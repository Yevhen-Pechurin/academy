# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Demo(models.Model):
    _name = 'demo.demo'
    _inherit = 'mail.thread'
    _description = 'demo.demo'

    name = fields.Char()
    salesperson = fields.Many2one('res.users',
                                  copy=False,
                                  tracking=True,
                                  string='Salesperson',
                                  default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Client', tracking=True)
    date = fields.Date(tracking=True)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], default='scheduled', tracking=True)
    description = fields.Text(tracking=True)


