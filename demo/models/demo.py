# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'Demo'
    # _inherit = "ir.sequence"
    _inherit = 'mail.thread'

    # name = fields.Char(required=True, compute="_compute_name")
    name = fields.Char(required=True, tracking=True)
    # saleperson = fields.Char(required=True, tracking=True, compute="_compute_saleperson")
    saleperson = fields.Many2one('res.users', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', tracking=True)
    # user_id = fields.Many2one('res.user', tracking=True)
    date = fields.Date(tracking=True)
    description = fields.Text(tracking=True)
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ("done", "Done"),
        ("canceled", "Canceled"),
        ], tracking=True, default="scheduled")
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'You can not have two users with the same name !')
    ]
