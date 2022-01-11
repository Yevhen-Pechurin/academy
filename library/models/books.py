from odoo import fields, models, api, _
from random import randint


class Tag(models.Model):
    _name = 'library.tags'
    _description = 'class for tags'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char()
    color = fields.Integer(default=_get_default_color)


class Author(models.Model):
    _name = 'library.authors'
    _description = 'class for authors'
    _inherit = 'mail.thread'

    @api.depends('books_ids')
    def _compute_books_id(self):
        for i in self:
            i.books_count = len(i.books_ids)

    name = fields.Char(tracking=True)
    books_ids = fields.One2many('library.book', 'authors_id', tracking=True)
    year = fields.Integer(tracking=True)
    books_count = fields.Integer(compute='_compute_books_id', store=True)


class BookHistory(models.Model):
    _name = 'library.history'
    _description = 'class for books history'

    books_id = fields.Many2one('library.book')
    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()
    end = fields.Boolean(default=False)


class BookInfo(models.Model):
    _name = 'library.info'
    _description = 'class for books info'
    _inherit = 'mail.thread'
    name = fields.Char(tracking=True)
    description = fields.Text(tracking=True)
    code = fields.Integer(tracking=True)
    authors_id = fields.Many2one('library.authors')
    tags = fields.Many2many('library.tags')


class Book(models.Model):
    _name = 'library.book'
    _description = 'class for books'
    _inherit = 'mail.thread'

    name = fields.Char(related='books_id.name')
    books_id = fields.Many2one('library.info')
    authors_id = fields.Many2one(related='books_id.authors_id')
    description = fields.Text(related='books_id.description')
    code = fields.Integer(related='books_id.code')
    tags = fields.Many2many(related='books_id.tags')
    status = fields.Selection([('ready', "Ready"),
                               ('are_used', 'Are Used'),
                               ('unavailable', 'Unavailable')], default='ready')
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('library.history', 'books_id')

    def action_on_hand(self):
        self.write({'status': 'are_used'})
        return {
            'name': _('On Hand'),
            'view_mode': 'form',
            'res_model': 'library.wizard.on_hand',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_get(self):
        self.write({'status': 'ready', 'partner_id': False})
        last_history = self.history_ids[-1]
        last_history.write({'end': True})

    @api.model_create_multi
    def create(self, vals_list):
        return super(Book, self).create(vals_list)

    def write(self, vals_list):
        return super(Book, self).write(vals_list)

    def _cron_overdue_messages(self):
        books = self.env["library.book"].search([])
        for book in books:
            last_history = book.history_ids
        if len(last_history) != 0:
            if book.status == 'are_used' and last_history[-1].due_date < fields.Date.today():
                book.message_post(body=f'{book.partner_id.name} верните книгу {book.name}',
                                  partner_ids=book.partner_id.ids, message_type='comment',subtype_id=self.env.ref('mail.mt_comment').id)
