# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _description = 'sale_origin.sale_origin'
    _inherit = 'product.template'
    country_of_origin = fields.Char(string='Country of Origin',)

class SaleOrderLine(models.Model):
    _description = 'sale_origin.line'
    _inherit = 'sale.order.line'
    country_of_origin = fields.Char(string='Country of Origin', related='product_id.country_of_origin')