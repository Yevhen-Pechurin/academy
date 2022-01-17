from odoo import fields, models, api, _


class Author(models.Model):
    _name = "library.author"
    _description = "Author"
    _inherit = 'mail.thread'

    name = fields.Char()
    country = fields.Many2one("res.country")
    city = fields.Char()
    birth_date = fields.Date()
    bio = fields.Text()
    image = fields.Image(string="Image", max_width=256, max_height=256)


class Language(models.Model):
    _name = "library.language"
    _description = "Language"

    name = fields.Char()


class Edition(models.Model):
    _name = "library.edition"
    _description = "Edition"
    _inherit = 'mail.thread'

    name = fields.Char()
    description = fields.Text()
    image = fields.Image(string="Image", max_width=256, max_height=256)


class Tag(models.Model):
    _name = "library.tag"
    _description = "Tag"

    name = fields.Char()


class History(models.Model):
    _name = "library.history"
    _description = "History"

    book_id = fields.Many2one("library.book")
    client_id = fields.Many2one("res.partner")
    date_on_hand = fields.Datetime()
    date_on_shelf = fields.Datetime()
    due_date = fields.Datetime()


class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    _inherit = 'mail.thread'

    name = fields.Char()
    description = fields.Text()
    author_id = fields.Many2one("library.author")
    image = fields.Image(string="Image", max_width=256, max_height=256)
    language_id = fields.Many2one("library.language")
    year_of_publication = fields.Integer()
    edition = fields.Many2one("library.edition")
    number = fields.Char()
    pages = fields.Integer()
    status = fields.Selection([
        ('on_hand', 'On Hand'),
        ('on_shelf', 'On Shelf'),
        ('not_available', 'Not Available'),
    ])
    tag_id = fields.Many2many("library.tag", tracking=True)
    cover = fields.Selection([
        ('hard', 'Hard Cover'),
        ('soft', 'Soft Cover'),
    ])
    client_id = fields.Many2one("res.partner")
    book_history_id = fields.One2many("library.history", "book_id")
    due_date = fields.Datetime()
    overdue_notification_date = fields.Datetime()

    _sql_constraints = [
        ('number_unique',
         'unique(number)',
         'Choose another value - it has to be unique!')
    ]

    def action_on_hand(self):
        return {
            'name': _('On Hand'),
            'view_mode': 'form',
            'res_model': 'library.book.on_hand',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_on_shelf(self):
        last_history = self.book_history_id[-1]
        if last_history:
            last_history.write({
                'date_on_shelf': fields.Datetime.now()
            })
        self.write({
            'status': 'on_shelf',
            'client_id': False
        })

    def overdue_notification(self):
        today = fields.Datetime.now()
        overdue_books = self.env['library.book'].search([
            ('status', '=', 'on_hand'),
            ('due_date', '<', today),
            ('overdue_notification_date', '!=', today)
        ])
        for book in overdue_books:
            body = '%s , термін користуваня книгою %s вийшов. Поверніть, будь ласка, книгу на полицю' % (
                book.client_id.name, book.name)
            subtype = self.env.ref('mail.mt_comment')
            book.message_post(body=body, partner_ids=book.client_id.ids, message_type='comment', subtype_id=subtype.id)
            book.write({
                'overdue_notification_date': fields.Datetime.now()
            })


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    books_count = fields.Integer(compute='_compute_books_count')

    def _compute_books_count(self):
        book_data = self.env['library.book'].read_group(
            domain=[('client_id', 'in', self.ids)],
            fields=['client_id'], groupby=['client_id']
        )
        self.books_count = 0
        for group in book_data:
            partner = self.browse(group['client_id'][0])
            partner.books_count = group['client_id_count']

    def show_books(self):
        self.ensure_one()
        return {
            'name': _('Client`s Books'),
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            'domain': [('client_id', '=', self.id)],
            'type': 'ir.actions.act_window',
        }
