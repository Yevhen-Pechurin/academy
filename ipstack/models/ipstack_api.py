# -*- coding: utf-8 -*-
import logging
import requests
from .api import IpstackApi
from odoo import models, fields, api
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
            return IpstackApi(key, url)
        else:
            raise UserError('Key for Ipstack not filled')

    def get_ip_data(self, ip):
        api = self.get_api()
        try:
            return api.get_ip_data(ip)
        except Exception as e:
            _logger.exception('Ipstack error: %s' % e)
            raise {}
