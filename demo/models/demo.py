# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Demo(models.Model):
    _name = 'demo.demo'
    # _inherit = 'mail.thread'
    _description = 'Demo'

    name = fields.Char()
    user_id = fields.Char()
    partner_id = fields.Many2one('res.partner')
    date = fields.Date()
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progres', 'In Progres'),
        ('done', 'Done'),
        ('сanceled', 'Canceled'),
    ], default='scheduled', compute='_compute_state', store=True, tracking=True)
    description = fields.Text()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_unig', 'unique (name)', """Only one name can be defined for each user!""")
    ]

    @api.depends('active')
    def _compute_state(self):
        for demo in self:
            if not demo.active:
                demo.state = 'unavailable'
            else:
                demo.state = demo.state
