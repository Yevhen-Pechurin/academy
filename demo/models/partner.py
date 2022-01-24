from odoo import fields, api, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'model for partner demo'

    demo_ids = fields.One2many('demo.demo', 'partner_id')
    demos_count = fields.Integer(compute='_compute_demos_count')

    @api.depends('demo_ids')
    def _compute_demos_count(self):
        self.demos_count = len(self.demo_ids)

    def get_demos(self):
        demos = self.demo_ids.ids
        return {
            'name': _('Client'),
            'view_mode': 'tree',
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', demos)]
        }
