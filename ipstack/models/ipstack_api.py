# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .api import IpStackAPI


class IpStack(models.Model):
    _name = 'ipstack.api'
    _description = 'ipstack.ipstack'

    def get_api(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        url = get_param('ip.stack.url', 'http://api.ipstack.com/')
