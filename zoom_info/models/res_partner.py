# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zoom_api_company_id = fields.Char('Zoom api company Id')

    @api.model
    def get_country(self, country_name, state_name):
        values = {}
        if country_name:
            values['country_id'] = self.env['res.country'].sudo().search([('name', '=', country_name)], limit=1).id
        if state_name:
            values['state_id'] = self.env['res.country.state'].sudo().search([('country_id', '=', values['country_id']), ('name', '=', state_name)]).id
        return values
