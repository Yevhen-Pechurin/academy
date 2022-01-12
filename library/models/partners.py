from odoo import fields, api, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    books_ids = fields.One2many('library.book', 'partner_id')
    books_count = fields.Integer(compute='_compute_line')

    @api.depends('books_ids')
    def _compute_line(self):
        self.books_count = len(self.books_ids)

    def actionget(self):
        books = self.books_ids.ids
        return {
            'name': _('User Books'),
            'view_mode': 'tree',
            'res_model': 'library.book',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', books)]

        }
