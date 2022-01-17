from odoo import fields, api, models, _
from random import randint


class History(models.Model):
    _name = 'library.history'
    _description = 'Class for book`s history'

    end = fields.Boolean()
    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()
    book_id = fields.Many2one('library.book')


class BookTag(models.Model):
    _name = 'library.tag'
    _description = 'Class for book`s tags'

    def _default_color(self):
        return randint(1, 11)

    name = fields.Char()
    color = fields.Integer(default=_default_color)


class Author(models.Model):
    _name = 'library.author'
    _description = 'Class for book`s author'
    _inherit = ['mail.thread']

    @api.depends('books_ids')
    def _compute_books_count(self):
        self.books_count = len(self.books_ids)

    name = fields.Char(tracking=True)
    year = fields.Integer(tracking=True)
    books_ids = fields.One2many('library.info', 'author_id', tracking=True)
    books_count = fields.Integer(readonly=True, compute='_compute_books_count', tracking=True)


class BookInfo(models.Model):
    _name = 'library.info'
    _description = 'Class for book`s info'
    _inherit = ['mail.thread']

    name = fields.Char(tracking=True)
    code = fields.Char(tracking=True)
    description = fields.Text(tracking=True)
    tags = fields.Many2many('library.tag', tracking=True)
    author_id = fields.Many2one('library.author', tracking=True)


class Book(models.Model):
    _name = 'library.book'
    _description = 'Class for books'
    _inherit = ['image.mixin', 'mail.thread']
    _inherits = {'library.info': 'book_id'}

    book_id = fields.Many2one('library.info', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('library.history', 'book_id', readonly=True)
    status = fields.Selection([
        ('ready', 'Ready'),
        ('on_hand', 'On Hand'),
        ('archived', 'Archived')
    ], default='ready')

    def action_on_hand(self):
        return {
            'name': _('On Hand'),
            'res_model': 'library.wizard.on_hand',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new'
        }

    def action_get(self):
        self.write({'status': 'ready', 'partner_id': False})
        self.history_ids[-1].end = True

    def _cron_overdue_messages(self):
        books = self.env['library.book'].search([])
        for book in books:
            last_history = book.history_ids[-1]
            if book.status == 'on_hand' and last_history.due_date < fields.Date.today():
                book.message_post(body=f'{book.partner_id.name} верните книгу {book.name}',
                                  partner_ids=book.partner_id.ids, message_type='comment',
                                  subtype_id=self.env.ref('mail.mt_comment').id)
