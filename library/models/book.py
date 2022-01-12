# -*- coding: utf-8 -*-

from odoo import models, fields, _


class Language(models.Model):
    _name = 'library.language'

    name = fields.Char()


class Author(models.Model):
    _name = 'library.author'
    _description = 'Author book'

    name = fields.Char()
    country_id = fields.Many2one('res.country')
    city = fields.Char()
    birthday = fields.Date()


class Tag(models.Model):
    _name = 'library.tag'

    name = fields.Char()


class Book(models.Model):
    _name = 'library.book'
    _inherit = 'mail.thread'
    _description = 'About Book'

    book_id = fields.Many2one('library.book.info')
    image = fields.Image(max_width=256, max_height=256)
    name = fields.Char(related='book_id.name', readonly=False)
    author = fields.Many2one(related='book_id.author')
    lang_id = fields.Many2one(related='book_id.lang_id')
    tag_ids = fields.Many2many(related='book_id.tag_ids')
    description = fields.Text(related='book_id.description')
    history_ids = fields.One2many('library.history', 'book_id')
    serial_number = fields.Char()
    status = fields.Selection([('on_shelf', 'On shelf'), ('on_hand', 'On hand'), ('scrap', 'Scrap'), ], default='on_shelf')
    partner_id = fields.Many2one('res.partner')
    publishing_house = fields.Many2many('res.company')
    pages = fields.Integer()
    year = fields.Integer()
    due_date = fields.Date()
    overdue_notification = fields.Date()

    _sql_constraints = [('number_uniq', 'unique (serial_number)', "Only one number can be defined for each books!")]

    def action_on_hand(self):
        return {
            'name': _('On Hand %s') % self.name,
            'view_mode': 'form',
            'res_model': 'library.wizard.on_hand',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_on_shelf(self):
        last_history = self.history_ids[-1]
        if last_history:
            last_history.write({
                'date_on_shelf': fields.Datetime.now()
            })
        self.write({
            'status': 'on_shelf',
            'partner_id': False
        })

    def _cron_overdue_book_notification(self):
        today = fields.Date.today()
        overdue_books = self.env['library.book'].search([
            ('status', '=', 'on_hand'),
            ('due_date', '>', today),
            ('overdue_notification', '!=', today)
        ])
        for book in overdue_books:
            body = f'{book.partner_id.name}, please return library book {book.name}'
            subtype=self.env.ref('mail.mt_comment')
            book.message_post(body=body, parent_ids=book.partner_id.ids, message_type='comment', subtype_id=subtype.id)
            book.write({
                'overdue_notification': fields.Datetime.now()
            })



class BookInfo(models.Model):
    _name = 'library.book.info'
    _inherit = 'mail.thread'
    _description = 'Info about Book'

    name = fields.Char()
    author = fields.Many2one('library.author', tracking=True)
    lang_id = fields.Many2one('library.language', tracking=True)
    tag_ids = fields.Many2many('library.tag', tracking=True)
    description = fields.Text(tracking=True)


class History(models.Model):
    _name = 'library.history'
    _description = 'History book'

    book_id = fields.Many2one('library.book')
    partner_id = fields.Many2one('res.partner')
    date_on_hand = fields.Date()
    date_on_shelf = fields.Date()
    due_date = fields.Date()

