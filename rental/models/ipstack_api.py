import logging
from odoo import models
from odoo.exceptions import UserError
from .api import IpstackAPI, BASE_URL

_logger = logging.getLogger(__name__)

class Ipstack(models.AbstractModel):
    _name = 'ipstack.api'
    _description = 'ipstack.ipstack'

    def build_API_request(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        base_url = get_param('ipstack.url', BASE_URL)
        key = get_param('ipstack.key')
        if key:
            return IpstackAPI(key, base_url)
        else:
            raise UserError('Key for Ipstack not filled')

    def get_ip_data(self, ip):
        api = self.build_API_request()
        try:
            return api.request_ip_data(ip)
        except Exception as e:
            _logger.exception('Ipstack error: %s' % e)
            return {}

