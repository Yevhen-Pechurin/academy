# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
from odoo.exceptions import UserError
from .api import IpStackAPI


_logger = logging.getLogger(__name__)


class IpStack(models.Model):
    _name = 'ipstack.api'
    _description = 'ipstack.ipstack'

    def get_api(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        url = get_param('ip.stack.url', 'http://api.ipstack.com/')
        key = get_param('ipstack.key')
        if key:
            return IpStackAPI(key, url)
        else:
            raise UserError('key for Ipstack not filled')


    def get_ip_data(self, ip):
        api = self.get_api()
        try:
            return api.get_ip_data(ip)
        except Exception as e:
            _logger.exception('Ipstack error %s' % e)
            return {}
