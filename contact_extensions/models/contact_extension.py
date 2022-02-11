# -*- coding: utf-8 -*-

from odoo import models, fields


class ContactExtension(models.Model):
    _description = 'Add field skype'
    _inherit = 'res.partner'

    skype = fields.Char(string="Skype")
    num_flat = fields.Integer(string="Number of flat", default=None)
