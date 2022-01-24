# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'Show demo field'
    _inherit = ['mail.thread']

    name = fields.Char(required=True, copy=False)
    user_id = fields.Many2one('demo.salesperson', 'demo_ids', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Client')
    date = fields.Date()
    status = fields.Selection([('scheduled', 'Scheduled'), ('in_progress', 'In Progress'), ('done', 'Done'), ('сanceled', 'Canceled'), ], default='scheduled',
        store=True, tracking=True)
    description = fields.Text()

    _sql_constraints = [
        ('field_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]


class SalesPerson(models.Model):
    _name = 'demo.salesperson'

    demo_ids = fields.One2many('demo.demo', 'user_id')
    name = fields.Char(string='Saleperson', required=True, default=lambda self: self.env.user.name)





