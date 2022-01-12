from odoo import fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    book_count = fields.Integer(compute='_compute_back_count')

