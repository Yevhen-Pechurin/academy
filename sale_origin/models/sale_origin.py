# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_of_origin = fields.Char(string='Country of origin')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    country_of_origin = fields.Char(string='Country of origin')