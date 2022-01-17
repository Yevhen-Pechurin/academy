# -*- coding: utf-8 -*-
from random import randint

from odoo import models, fields, api, _


# class Author(models.Model):
#     _name = 'library.author'
#     _description = 'Author'
#
#     name = fields.Char()
#     country_id = fields.Many2one('res.country')
#     city = fields.Char()
#     birthday_date = fields.Date()
#
#
# class Language(models.Model):
#     _name = 'library.language'
#     _description = 'Language'
#
#     name = fields.Char()
#
#
# class Tag(models.Model):
#     _name = 'library.tag'
#     _description = 'Tag'
#
#     def _get_default_color(self):
#         return randint(1, 11)
#
#     name = fields.Char()
#     color = fields.Integer('Color', default=_get_default_color)


class History(models.Model):
    _name = 'rental.history'
    _description = 'History'

    car_id = fields.Many2one('rental_car.car')
    partner_id = fields.Many2one('res.partner')
    date_on_hand = fields.Datetime()
    date_on_shelf = fields.Datetime()
    due_date = fields.Date()


# class BookInfo(models.Model):
#     _name = 'library.book.info'
#     _inherit = 'mail.thread'
#     _description = 'Book Info'
#
#     name = fields.Char(tracking=True)
#     author_id = fields.Many2one('library.author', tracking=True)
#     lang_id = fields.Many2one('library.language', tracking=True)
#     tag_ids = fields.Many2many('library.tag', tracking=True)
#     tag2_ids = fields.Many2many(comodel_name='library.tag', relation='rel_tag2', column1='book_id', column2='tag_id', tracking=True)
#     description = fields.Text(tracking=True, index=True)


class Car(models.Model):
    _name = 'rental.car'
    _inherit = 'mail.thread'
    # _inherits = {'library.book.info': 'book_id'}
    _description = 'Car'

    name = fields.Char(tracking=True)
    # book_id = fields.Many2one('library.book.info', required=True, ondelete="cascade")
    number = fields.Char(copy=False)
    model = fields.Char(copy=False)
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In Garage'),
        ('on_loan', 'On Loan'),
        ('under_repair', 'Under Repair'),
        ('unavailable', 'Unavailable'),
    ], default='in_garage', compute='_compute_status',
        store=True, tracking=True)
    rental_start_date = fields.Date()
    partner_id = fields.Many2one('res.partner')
    history_ids = fields.One2many('rental.history', 'car_id')
    # publishing_house_id = fields.Many2one('res.partner')
    image = fields.Image(string="Image", max_width=256, max_height=256)
    # due_date = fields.Date()
    # overdue_notification_date = fields.Date()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('number_uniq', 'unique (number)', """Only one number can be defined for each car!"""),
    ]

    def action_on_hand(self):
        return {
            'name': _('On Hand %s') % self.name,
            'view_mode': 'form',
            'res_model': 'library.wizard.on_hand',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }
    #
    # def action_on_shelf(self):
    #     last_history = self.history_ids[-1]
    #     if last_history:
    #         last_history.write({
    #             'date_on_shelf': fields.Datetime.now()
    #         })
    #     self.sudo().write({
    #         'status': 'on_shelf',
    #         'partner_id': False
    #     })
    #
    # def _cron_overdue_book_notification(self):
    #     today = fields.Date.today()
    #     overdue_books = self.env['library.book'].search([
    #         ('status', '=', 'on_hand'),
    #         ('due_date', '<', today),
    #         ('overdue_notification_date', '!=', today)
    #     ])
    #     for book in overdue_books:
    #         body = '%s пожалуйста верните книгу %s' % (book.partner_id.name, book.name)
    #         subtype = self.env.ref('mail.mt_comment')
    #         book.message_post(body=body, partner_ids=book.partner_id.ids, message_type='comment', subtype_id=subtype.id)
    #         book.write({
    #             'overdue_notification_date': fields.Datetime.now()
    #         })
    #
    # @api.depends('active')
    # def _compute_status(self):
    #     for car in self:
    #         if not car.active:
    #             car.status = 'unavailable'
    #         else:
    #             car.status = 'in_garage'
