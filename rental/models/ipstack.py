
import logging
from .api import IpStackApi
from odoo import models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class Ipstack(models.AbstractModel):
    _name = 'ipstack.api'
    _description = 'ipstack.ipstack'

    def get_api(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        url = get_param('ipstack.url', 'http://api.ipstack.com/')
        key = get_param('ipstack.key')
        if key:
            return IpStackApi(key, url)
        else:
            raise UserError('Key for Ipstack not found')

    def get_api_data(self, ip):
        api = self.get_api()
        try:
            return api.get_data(ip)
        except Exception as e:
            _logger.exception('Ipstack error: %s' % e)
            return