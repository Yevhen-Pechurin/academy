from odoo import fields, models


class PPE(models.Model):
    _name = 'bluesky_mrp_workorder.ppe'
    _table = 'bluesky_mrp_production_ppe'
    _description = "PPE"

    name = fields.Char(
        "Name",
        required=True,
    )

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Name must be unique !'),
    ]
