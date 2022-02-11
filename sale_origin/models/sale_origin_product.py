# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _description = 'sale_origin.sale_origin'
    _inherit = 'product.template'
    country_of_origin = fields.Char(string='Country of Origin', default=None)
    min_temperature_regime = fields.Integer()
    max_temperature_regime = fields.Integer()
    temperature_regime = fields.Char(compute='_compute_temperature_regime', store=True)

    @api.depends('min_temperature_regime', 'max_temperature_regime')
    def _compute_temperature_regime(self):
        for i in self:
            i.temperature_regime = str(i.min_temperature_regime) + '-' + str(i.max_temperature_regime)


