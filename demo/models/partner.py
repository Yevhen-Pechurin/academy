from odoo import fields, api, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def call_wizard_demo(self):
        return {
            'name': _('Create Demo'),
            'res_model': 'demo.wizard.demo',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new'
        }