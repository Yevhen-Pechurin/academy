from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    demo_count = fields.Integer(compute='_compute_demo_count')

    def _compute_demo_count(self):
        demo_data = self.env['demo.demo'].read_group(
            domain=[('partner_id', 'in', self.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        self.demo_count = 0
        for group in demo_data:
            partner = self.browse(group['partner_id'][0])
            partner.demo_count = group['partner_id_count']


    def action_view_demo(self):
        self.ensure_one()
        return {
            'name': _('Partners Demos'),
            'view_mode': 'tree,form',
            'res_model': 'demo.demo',
            'domain': [('partner_id', '=', self.id)],
            'type': 'ir.actions.act_window'
            # 'context': {'search_default_client_id': self.id}
        }

    def action_new_demo(self):
        return {
            'name': _('Partners New Demo'),
            'view_mode': 'form',
            'res_model': 'demo.demo',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }