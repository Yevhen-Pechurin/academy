# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Demo(models.Model):
    _name = 'demo.demo'
    _inherit = 'mail.thread'
    _description = 'demo.demo'

    name = fields.Char(copy=False, readonly=True, default='New', required=True)
    salesperson = fields.Many2one('res.users',
                                  copy=False,
                                  tracking=True,
                                  string='Salesperson',
                                  default=lambda self: self.env.user, required=True)
    partner_id = fields.Many2one('res.partner', string='Client', tracking=True)
    date = fields.Date(tracking=True)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], default='scheduled', tracking=True, required=True)
    description = fields.Text(tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('demo.demo') or _('New')
        return super(Demo, self).create(vals)
