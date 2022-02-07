from odoo import fields, api, _, models


class ProductTemplate(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    country_of_origin = fields.Char(related='product_template_id.country_of_origin')
