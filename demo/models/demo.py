# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'Show demo field'
    _inherit = ['mail.thread']

    name = fields.Char(required=True, copy=False, tracking=True, default='New Demo')
    user_id = fields.Many2one('res.users', 'Salesperson', default=lambda self: self.env.user.id, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Client', tracking=True)
    date = fields.Date(tracking=True)
    status = fields.Selection(
        [('scheduled', 'Scheduled'), ('in_progress', 'In Progress'), ('done', 'Done'), ('сanceled', 'Canceled'), ],
        default='scheduled', tracking=True)
    description = fields.Text(tracking=True)
    #
    # _sql_constraints = [
    #     ('field_unique',
    #      'unique(name)',
    #      'Choose another value - it has to be unique!')
    # ]

    @api.model
    def create(self, vals):
        if vals.get('name', 'New Demo') == "New Demo":
            vals['name'] = self.env['ir.sequence'].next_by_code('demo.demo') or _('New')
        result = super(Demo, self).create(vals)
        return result

