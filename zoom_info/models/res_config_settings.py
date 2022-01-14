# -*- coding: utf-8 -*-

import re
import logging

from odoo import api, fields, models
from ..zoom_info_api.main import send_request
import base64
import requests

_logger = logging.getLogger(__name__)


def english_check(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('params'):
            for key, value in kwargs['params'].items():
                if key == 'matchPersonInput':
                    for k, v in value[0].items():
                        if re.compile(r'[a-zA-Z0-9_.]').match(str(v)) is None:
                            return []
                elif isinstance(value, str) and re.compile(r'[a-zA-Z0-9_.]').match(str(value)) is None:
                    return []
            return func(*args, **kwargs)

    return wrapper


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_zoom_info = fields.Boolean(
        string='Allow the users to synchronize with Zoom Info')
    zi_username = fields.Char("Zoom Info Username")
    zi_password = fields.Char("Zoom Info Password")
    zi_token = fields.Char()
    is_zi_token_generated = fields.Boolean(string='Refresh Token Generated')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrDefault = self.env['ir.default'].sudo()
        IrDefault.set('res.config.settings', 'zi_username', self.zi_username)
        IrDefault.set('res.config.settings', 'zi_password', self.zi_password)
        IrDefault.set('res.config.settings', 'zi_token', self.zi_token)
        IrDefault.set('res.config.settings', 'is_zi_token_generated', self.is_zi_token_generated)

        if self.zi_username and self.zi_password:
            params = {'username': self.zi_username, 'password': self.zi_password}
            zi_token = send_request('authenticate', params, authorization=True)
            IrDefault.set('res.config.settings', 'zi_token', zi_token['jwt'])
            IrDefault.set('res.config.settings', 'is_zi_token_generated', True)
        return True

    # @api.depends('zi_username', 'zi_password')
    # def _compute_zoom_info_token(self) -> None:
    #     params = self.env['ir.config_parameter'].sudo()
    #     zi_username = params.get_param('zi_username', False)
    #     zi_password = params.get_param('zi_password', False)
    #     zi_token = send_request('authenticate', {'zi_username': zi_username, 'zi_password': zi_password})
    #     for config in self:
    #         config.zi_token = zi_token
    #         config.zi_password = True

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        res.update(
            {
                'zi_username': IrDefault.get('res.config.settings', 'zi_username') or None,
                'zi_password': IrDefault.get('res.config.settings', 'zi_password') or None,
                'zi_token': IrDefault.get('res.config.settings', 'zi_token') or None,
                'is_zi_token_generated': IrDefault.get('res.config.settings', 'is_zi_token_generated') or False,
            }
        )

        return res

    def update_token(self):
        _logger.info('ZoomInfo updating token.')
        params = self.env['ir.default'].sudo()
        zi_token_before = params.get('res.config.settings', 'zi_token')
        zi_username = params.get('res.config.settings', 'zi_username')
        zi_password = params.get('res.config.settings', 'zi_password')
        zi_token = send_request(uri='authenticate', method='POST', params={
            'username': zi_username,
            'password': zi_password
        }, authorization=True, headers={})
        if zi_token['jwt'] != zi_token_before:
            params.set('res.config.settings', 'zi_token', zi_token['jwt'])
            return zi_token['jwt']
        return None

    @english_check
    def zoom_info_request(self, uri: str, params: dict, headers: dict = None, authorization: bool = False,
                          method: str = 'POST', preuri: str = None, timeout: str = None):
        headers = headers and headers or {}
        headers.update(
            {'Authorization': f"Bearer {self.env['ir.default'].sudo().get('res.config.settings', 'zi_token')}"})
        res = send_request(uri=uri, params=params, headers=headers, authorization=authorization,
                           method=method, preuri=preuri, timeout=timeout)
        if res.get('content') == 'Unauthorized':
            self.update_token()
            return self.zoom_info_request(uri=uri, params=params, headers=headers, authorization=authorization,
                                          method=method, preuri=preuri, timeout=timeout)
        _logger.info('ZoomInfo response successfully.')

        try:
            res['data']['result'][0]['data'][0]['picture'] = base64.b64encode(
                requests.get(res['data']['result'][0]['data'][0]['picture']).content)
            res['data']['result'][0]['data'][0]['logo'] = base64.b64encode(
                requests.get(res['data']['result'][0]['data'][0]['logo']).content)
        except:
            pass

        try:
            res['data']['result'][0]['data'][0]['logo'] = base64.b64encode(
                requests.get(res['data']['result'][0]['data'][0]['logo']).content)
        except:
            pass

        return res
