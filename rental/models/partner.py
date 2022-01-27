from odoo import fields, api, models, _


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    cars_ids = fields.One2many('rental.car', 'partner_id')
    cars_count = fields.Integer(compute='_compute_cars_count')
    ip = fields.Char()

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

    @api.onchange('ip')
    def get_data(self):
        data = self.env['ipstack.api'].get_api_data(self.ip)
        if data:
            country = self.env['res.country'].search([
                ('code', '=', data['country_code'])
            ], limit=1)
            self.update({'city': data['city'],
            'zip': data['zip'],
            'country_id': country.id})
