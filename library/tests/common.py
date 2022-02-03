from odoo.addons.base.tests.common import TransactionCase


class TestBookCommonBase(TransactionCase):

    def setUp(self):
        super(TestBookCommonBase, self).setUp()
        self.BookInfo = self.env['library.book.info']
        self.Book = self.env['library.book']
        self.Author = self.env['library.author']
        self.Partner = self.env['res.partner']

        self.partner_1 = self.Partner.create({
            'name': 'Test Partner',
        })

        self.book_info_1 = self.BookInfo.create({
            'name': 'Harry Potter and the Order of the Phoenix',
        })

        self.env['ir.sequence'].search([
            ('code', '=', 'library.book'),
        ]).write({
            'number_next': 1,
            'padding': 6,
        })


        self.book_1 = self.Book.create({
            'book_id': self.book_info_1.id,
            'status': 'on_hand',
            'client_id': self.partner_1.id
        })

        self.book_2 = self.Book.create({
            'book_id': self.book_info_1.id,
            'status': 'on_shelf',
            'client_id': self.partner_1.id
        })




# -c /home/olga/PycharmProjects/academy/odoo.conf
# --test-enable -d library -i library --log-level=test --stop-after-init --test-tags book --dev=xml