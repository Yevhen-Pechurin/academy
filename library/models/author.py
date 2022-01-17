# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Author(models.Model):
    _name = "library.author"
    _description = "Author"

    name = fields.Char()
    country_id = fields.Many2one('res.country')
    year_birth = fields.Date()
    year_death = fields.Date()
    # books =
    description = fields.Text