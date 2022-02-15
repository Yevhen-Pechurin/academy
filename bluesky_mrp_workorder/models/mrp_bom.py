from odoo import fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    product_specification = fields.Binary(
        'PDF of Product Specification',
        attachment=True,
        help="Upload your PDF file.",
    )
