from odoo import fields, models


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    worksheet = fields.Binary(
        related='production_id.bom_id.product_specification',
    )
    worksheet_old = fields.Binary(
        related='operation_id.worksheet',
        readonly=True,
    )
