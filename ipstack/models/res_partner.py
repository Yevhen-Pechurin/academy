from odoo import models, fields, api


class ReaPartner(models.Model):
    _inherit = 'res.partner'

    ip = fields.Char()

    @api.onchange('ip')
    def check_ip(self):
        if self.ip:
            data = self.env['ipstack.api'].get_ip_data(self.ip)
            if data:
                self.update(self.prepare_data(data))

    def prepare_data(self, data):
        country = self.env['res.country'].search([
            ('code', '=', data['country_code'])
        ], limit=1)
        return {
            'city': data['city'],
            'zip': data['zip'],
            'country_id': country.id
        }
