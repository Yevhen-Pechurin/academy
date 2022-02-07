from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_of_origin = fields.Char()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    country_of_origin = fields.Char(related='product_template_id.country_of_origin')
