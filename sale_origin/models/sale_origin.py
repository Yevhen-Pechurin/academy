from odoo import fields, models, api, _

class SaleOrigin(models.Model):
    _name = "product.template"
    _inherit = 'product.template'
    _description = "Country of origin"

    country_of_origin = fields.Many2one('res.country' , required=True)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    country_of_origin = fields.Many2one(related="product_template_id.country_of_origin")


