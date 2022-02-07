from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    zi_username = fields.Char("Zoom Info Username", config_parameter='zoom_info.username')
    zi_password = fields.Char("Zoom Info Password", config_parameter='zoom_info.password')
    zi_token = fields.Char(config_parameter='zoom_info.token')