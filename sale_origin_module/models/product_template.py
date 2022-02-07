from odoo import fields, api, _, models


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    country_of_origin = fields.Char(default='None')
