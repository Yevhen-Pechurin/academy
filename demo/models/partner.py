from odoo import fields, api, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    demoes_ids = fields.One2many('demo.demo', 'partner_id')
    demoes_count = fields.Integer(compute='_compute_demo')

    @api.depends('demoes_ids')
    def _compute_demo(self):
        self.demoes_count = len(self.demoes_ids)

    def call_wizard_demo(self):
        return {
            'name': _('Create Demo'),
            'res_model': 'demo.wizard.demo',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new'
        }

    def demo_get(self):
        ids = self.demoes_ids.ids
        return {
            'name': _('User Demoes'),
            'view_mode': 'tree',
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', ids)]

        }
