from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ip = fields.Char()

    @api.onchange('ip')
    def check_ip(self):
        if self.ip:
            data = self.env['ipstack.api'].get_ip_data(self.ip)
        if data:
            country = self.env['res.partner'].search([
                'code', '=', data['country_code']
            ], limit=1)
            self.update({
                'city': data['city'],
                'zip': data['zip'],
                'country_id': country.id

            })
