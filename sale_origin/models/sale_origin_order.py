from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    country_of_origin = fields.Char(string='Country of Origin', related='product_id.country_of_origin')
    temperature_regime = fields.Char(related='product_id.temperature_regime')

    def get_sale_order_line_multiline_description_sale(self, product):
        return _(f'{super(SaleOrderLine, self).get_sale_order_line_multiline_description_sale(product)}\nTemperature:{self.temperature_regime}')