from odoo import api, fields, models


class ComponentRequirement(models.Model):
    _name = 'bluesky_mrp_workorder.component_requirement'
    _description = "Component Requirements"

    mo_id = fields.Many2one(
        'mrp.production',
        "Manufacturing Order",
        required=True,
        ondelete='cascade',
    )
    product_id = fields.Many2one(
        'product.product',
        "Product",
        required=True,
        ondelete='cascade',
    )
    uom_id = fields.Many2one(
        'uom.uom',
        "Unit of Measure",
        required=True,
    )
    consumed_qty = fields.Float(
        "BOM qty",
        compute="_compute_consumed_qty",
    )
    picked_qty = fields.Float(
        "Picked",
    )
    returned_qty = fields.Float(
        "Returned",
    )
    rejected_qty = fields.Float(
        "Rejected",
    )
    sent_to_client_qty = fields.Float(
        "Sent To Client",
    )
    variance_qty = fields.Float(
        "Variance",
        compute="_compute_variance_qty",
        store=True,
    )

    @api.depends(
        'mo_id.move_raw_ids.product_id', 'uom_id', 'mo_id.move_raw_ids.product_uom',
        'mo_id.move_raw_ids.product_uom_qty',
    )
    def _compute_consumed_qty(self):
        StockMove = self.env['stock.move']
        new_keys = self.mo_id._get_raw_moves_requirements_key()
        for r in self:
            raw_moves = new_keys.get((r.mo_id, r.product_id, r.uom_id), StockMove)
            r.consumed_qty = sum(raw_moves.mapped('product_uom_qty'))

    @api.depends('picked_qty', 'rejected_qty', 'sent_to_client_qty')
    def _compute_variance_qty(self):
        for record in self:
            record.variance_qty = record.picked_qty - record.rejected_qty - record.sent_to_client_qty
