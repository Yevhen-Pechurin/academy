# -*- coding: utf-8 -*-
from random import randint

from odoo import models, fields, _, api


class Author(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char()
    country_id = fields.Many2one('res.country')
    city = fields.Char()
    birthday_data = fields.Date()


class Language(models.Model):
    _name = 'library.language'
    _description = 'Language'

    name = fields.Char()


class Tag(models.Model):
    _name = 'library.tag'
    _description = 'Tag'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color', default=_get_default_color)

    _sql_constraints = [
        ('name_unig', 'unique (name)', "Tag name already exists!")
    ]


class PublishingHouse(models.Model):
    _name = 'library.publishing.house'
    _description = 'Publishing House'

    name = fields.Char()


class History(models.Model):
    _name = 'library.history'
    _description = 'History'

    book_id = fields.Many2one('library.book')
    partner_id = fields.Many2one('res.partner')
    date_on_hand = fields.Date()
    date_on_shelf = fields.Date()
    due_date = fields.Date()


class BookInfo(models.Model):
    _name = 'library.book.info'
    _inherit = 'mail.thread'
    _description = 'Book Info'

    name = fields.Char(tracking=True)
    author_id = fields.Many2one('library.author', tracking=True)
    lang_id = fields.Many2one('library.language', tracking=True)
    tag_ids = fields.Many2many('library.tag', tracking=True)
    tag2_ids = fields.Many2many(comodel_name='library.tag', relation='rel_teg2', column2='tag_id', tracking=True)
    description = fields.Text(tracking=True)


class Book(models.Model):
    _name = 'library.book'
    _inherit = 'mail.thread'
    _description = 'Book'

    book_id = fields.Many2one('library.book.info')
    name = fields.Char(related='book_id.name', readonly=False)
    number = fields.Char(copy=False)
    author_id = fields.Many2one(related='book_id.author_id')
    year = fields.Integer()
    lang_id = fields.Many2one(related='book_id.lang_id')
    status = fields.Selection([
        ('on_shelf', 'On Shelf'),
        ('on_hand', 'On Hand'),
        ('unavailable', 'Unavailable'),
    ], default='on_shelf', compute='_compute_status', store=True, tracking=True)
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('library.history', 'book_id')
    tag_ids = fields.Many2many(related='book_id.tag_ids')
    publishing_house_id = fields.Many2one('res.partner')
    image = fields.Image(string="Image", max_width=256, max_height=256, help="Select image here", verify_resolution=True)
    description = fields.Text(related='book_id.description')
    due_date = fields.Date()
    overdue_notification_date = fields.Date()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('number_unig', 'unique (number)', """Only one number can be defined for each book!""")
    ]

    def action_on_hand(self):
        return {
            'name': _('On Hand %s') % self.name,
            'view_mode': 'form',
            'res_model': 'library.wizard.on_hand',
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
            ('due_date', '<', today),
            ('overdue_notification_date', '!=', today)
        ])
        for book in overdue_books:
            body = '%s Пожалуйста, верните книгу. %s' % (book.partner_id.name, book.name)
            subtype = self.env.ref('mail.mt_comment')
            book.message_post(body=body, partner_ids=book.partner_id.ids, message_type='comment', subtype_id=subtype.id)
            book.write({
                'overdue_notification_date': fields.Datetime.now()
            })

    @api.depends('active')
    def _compute_status(self):
        for book in self:
            if not book.active:
                book.status = 'unavailable'
            else:
                book.status = 'on_shelf'
