from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ipstack_key = fields.Char(config_parameter='ipstack.key')