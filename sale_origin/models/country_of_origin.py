# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrigin(models.Model):
    _name = 'sale_origin.country_of_origin'
    _description = 'sale_origin.sale_origin'
    country_of_origin = fields.Char(string='Country of Origin',)