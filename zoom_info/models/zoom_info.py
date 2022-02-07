import base64
import logging
import requests
from requests import HTTPError

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from .zoom_api import ZoomApi

_logger = logging.getLogger(__name__)


class ZoomInfo(models.AbstractModel):
    _name = 'zoom.info'
    _description = 'Zoom Info'

    def get_zoom_api(self, update_token=False):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        token = get_param('zoom_info.token')
        if token and not update_token:
            return ZoomApi(token)
        else:
            zi_username = get_param('zoom_info.username')
            zi_password = get_param('zoom_info.password')
            if zi_username and zi_password:
                try:
                    zoom_api = ZoomApi(username=zi_username, password=zi_password)
                    zi_token = zoom_api.get_authentification_token()
                except Exception as e:
                    _logger.exception('Zoom Info error: %s' % e)
                    return None
                else:
                    self.env['ir.config_parameter'].sudo().set_param('zoom_info.token', zi_token)
                    return zoom_api
            else:
                raise UserError(_('Password or Login not filled for Zoom Info'))

    @api.model
    def update_token(self):
        params = self.env['ir.default'].sudo()
        zi_token_before = params.get('res.config.settings', 'zi_token')
        zi_username = params.get('res.config.settings', 'zi_username')
        zi_password = params.get('res.config.settings', 'zi_password')
        zoom_api = ZoomApi(username=zi_username, password=zi_password)
        zi_token = zoom_api.get_authentification_token()
        if zi_token != zi_token_before:
            params.set('res.config.settings', 'zi_token', zi_token)
            return zi_token
        return None

    def zoom_info_request(self, url, params=None) -> dict:
        zoom_api = self.get_zoom_api()
        if zoom_api is None:
            return {}
        try:
            response = zoom_api.send_request(url, params)
        except HTTPError as e:
            _logger.error('Zoom info request with param: \n %s \nerror: %s' % (params, e))
            return {}
        if response.get('error') == 'Unauthorized':
            zoom_api = self.get_zoom_api(update_token=True)
            if zoom_api is None:
                return {}
            response = zoom_api.send_request(url, params)
        return response['data']

    @api.model
    def find_company_id(self, name):
        params = {"companyName": name}
        return self.zoom_info_request('/search/company', params)

    @api.model
    def find_company_info(self, company_id):
        params = {
            "matchCompanyInput": [{"companyId": company_id}],
            "outputFields": [
                "name",
                "street",
                "city",
                "state",
                "zipCode",
                "country",
                "phone",
                "website",
                "logo",
            ]
        }
        response = self.zoom_info_request('/enrich/company', params)
        res = response['result'][0]['data'][0]
        logo = ''
        if res['logo']:
            try:
                logo = base64.b64encode(requests.get(res['logo']).content)
            except Exception as e:
                _logger.exception('Zoom Info getting picture error from url %s' % res['logo'])
        country_state = self.get_country_state(res['country'], res['state'])
        res.update({
            'logo': logo,
            'country': country_state['country_id'],
            'state': country_state['state_id'],
        })
        return res

    @api.model
    def find_contact_by_name(self, name, company_id):
        params = {
            "fullName": name,
            "companyId": company_id,
        }
        response = self.zoom_info_request('/search/contact', params)
        return response

    @api.model
    def find_contact_by_position(self, job_title, company_id):
        params = {
            "jobTitle": job_title,
            "companyId": company_id,
        }
        response = self.zoom_info_request('/search/contact', params)
        return response

    @api.model
    def find_contact_info(self, person_id):
        params = {
            "matchPersonInput": [{"personId": person_id}],
            "outputFields": [
                "firstName",
                "lastName",
                "email",
                "phone",
                "jobTitle",
                "picture",
            ]
        }
        response = self.zoom_info_request('/enrich/contact', params)
        res = response['result'][0]['data'][0]
        res.update({
            'picture': res['picture'] and base64.b64encode(requests.get(res['picture']).content or ''),
            'name': ' '.join([res['firstName'], res['lastName']])
        })
        return res

    @api.model
    def get_country_state(self, country_name, state_name):
        values = {}
        if country_name:
            values['country_id'] = self.env['res.country'].sudo().search([('name', '=', country_name)], limit=1).id
        if state_name:
            values['state_id'] = self.env['res.country.state'].sudo().search([('country_id', '=', values['country_id']), ('name', '=', state_name)]).id
        return values
