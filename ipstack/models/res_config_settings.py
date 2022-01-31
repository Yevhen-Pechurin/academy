from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ipstack_key = fields.Char(config_parameter='ipstack.key')
