# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'demo.demo'

    name = fields.Char()
    salesperson = fields.Many2one('res.users', copy=False, tracking=True,
                                      string='Salesperson',
                                      default=lambda self: self.env.user)
    description = fields.Text()
    partner_id = fields.Many2one('res.partner', string='Client', tracking=True)
    date = fields.Date(tracking=True)
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], default='scheduled', tracking=True)
    description = fields.Text(tracking=True)

