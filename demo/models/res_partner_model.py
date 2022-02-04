from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    demos_count = fields.Integer(compute='_compute_demo_count')

    @api.depends('demos_count')
    def _compute_demo_count(self):
        demo = self.env['demo.demo'].read_group(
            domain=[('partner_id', 'in', self.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        self.demos_count = 0
        for group in demo:
            partner = self.browse(group['partner_id'][0])
            partner.demos_count = group['partner_id_count']

    def show_demos(self):
        self.ensure_one()
        return {
            'name': _('Client`s Demos'),
            'view_mode': 'kanban,tree,form',
            'res_model': 'demo.demo',
            'domain': [('partner_id', '=', self.id)],
            'type': 'ir.actions.act_window',
        }
    def create_new_demo(self):
        return {
            'name': _('New Demo'),
            'view_mode': 'form',
            'res_model': 'demo.demo.create',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }