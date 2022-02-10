# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _description = 'sale_origin.line'
    _inherit = 'sale.order.line'
    country_of_origin = fields.Char(string='Country of Origin', related='product_id.country_of_origin')
    temperature_regime = fields.Char(related='product_id.temperature_regime')

