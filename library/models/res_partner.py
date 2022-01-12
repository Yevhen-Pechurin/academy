# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class BooksAtClient(models.Model):
    # _name = 'clients_book'
    _inherit = 'res.partner'
    # _description = 'Book clients'

    book_order_count = fields.Integer(compute='_compute_book_count', string='Book Order Count')

    def _compute_book_count(self):
        # pass
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        book_order_groups = self.env['library.book'].read_group(
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        partners = self.browse()
        for group in book_order_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.book_order_count += group['partner_id_count']
                    partners |= partner
                partner = partner.parent_id
        (self - partners).book_order_count = 0

