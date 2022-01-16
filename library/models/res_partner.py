from odoo import models, fields, _

class ContactBookCount(models.Model):
    _inherit = 'res.partner'

    books_count = fields.Integer(compute='_compute_book_count')

    def _compute_books_count(self):
        books_data = self.env['library.book'].read_group(
            domain=[('partner_id', 'in', self.ids)],
            fields=['partner_id'], groupby='partner_id'
        )
        self.books_count = 0
        for group in books_data:
            partner = self.browse(group['partner_id'][0])
            partner.books_count = group['partner_id_count']

    def action_books_count(self):
        self.ensure_one()
        return {
            'name': _('Borrowed books'),
            'view_mode': 'tree,form',
            'res_model': 'library.books',
            'domain': [('partner_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            #alternatively, instead of domain:                note: unlike domain, this won't work as a filter as far as UI is concerned
            #'context': {'search_default_partner_id': self.id}
        }