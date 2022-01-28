# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Demo(models.Model):
    _name = 'demo.demo'
    _inherit = 'mail.thread'
    _description = 'Demo soft'

    name = fields.Char(readonly=False, tracking=True)
    salesperson = fields.Char(tracking=True)  # user_id =
    partner_id = fields.Many2one('res.partner', tracking=True)  # client
    date = fields.Date()
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], group_expand='_expand_states', store=True, tracking=True)  # default='scheduled',
    description = fields.Text(tracking=True)


    _sql_constraints = [
        ('name_unig', 'unique (name)', """Only one name can be defined for each demo!""")
    ]

    def _expand_states(self, states, domain, order):
        return[key for key, val in type(self).state.selection]
