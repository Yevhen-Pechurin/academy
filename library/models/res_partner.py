from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    book_count = fields.Integer(compute='_compute_book_count')

    def _compute_book_count(self):
        books_data = self.env['library.book'].read_group(
            domain=[('client_id', 'in', self.ids)],
            fields=['client_id'], groupby=['client_id']
        )
        self.book_count = 0
        for group in books_data:
            partner = self.browse(group['client_id'][0])
            partner.book_count = group['client_id_count']

    def action_view_books(self):
        self.ensure_one()
        return {
            'name': _('Partners Books'),
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            # 'domain': [('partner_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'search_default_client_id': self.id}
        }