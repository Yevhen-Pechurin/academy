# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_of_origin = fields.Many2one('res.country')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    country_of_origin = fields.Many2one(related='product_template_id.country_of_origin')
