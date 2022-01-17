# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .author import Author


class History(models.Model):
    _name = 'library.history'

    book = fields.Many2one("library.book")
    partner_id = fields.Many2one('res.partner')
    date_on_hand = fields.Date()
    date_on_shelf = fields.Date()


class Tag(models.Model):
    _name = "library.tag"

    name = fields.Char()
    name2 = fields.Text()

class Book(models.Model):
    _name = "library.book"
    _description = "for book"
    _inherit = 'mail.thread'

    name = fields.Char(tracking=True)
    year_of_edition = fields.Date()
    description = fields.Text()
    author_id = fields.Many2one("library.author")
    editor = fields.Char()
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ("done", "Done"),
        ("canceled", "Canceled"),
    ], default='draft')
    serial_number = fields.Char()
    partner_id = fields.Many2one('res.partner')
    # partner_ids = fields.One2many('library.history', 'book_id')
    # tag_ids = fields.Many2many('library.tag')
    tag_ids = fields.Many2many('library.tag', tracking=True)
    image = fields.Image(string='image', max_width=256, max_height=256)

    def action_in_progress(self):
        self.write({'status': 'in_progress'})

    def action_done(self):
        self.write({'status': 'done'})

    def action_on_hand(self):
        return {
            "name": "On Hand %s" % self.name,
            'view_mode': "form",
            'res_model': "library.wizard.on_hand",
            'type': 'ir.actions.act_window',
            'target': "new",
            }
