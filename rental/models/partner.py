from odoo import fields, api, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    cars_ids = fields.One2many('rental.car', 'partner_id')
    cars_count = fields.Integer(compute='_compute_cars_count')

    @api.depends('cars_ids')
    def _compute_cars_count(self):
        self.cars_count = len(self.cars_ids)

    def getcars(self):
        cars = self.cars_ids.ids
        return {
            'name': _('User Cars'),
            'view_mode': 'tree',
            'res_model': 'rental.car',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', cars)]
        }
