# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Demo(models.Model):
    _name = 'demo.demo'
    # _inherit = 'mail.thread'
    _description = 'Demo'

    name = fields.Char(tracking=True)
    user_id = fields.Many2one('res.users', string='User Id', tracking=True,  default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', tracking=True)
    date = fields.Date(tracking=True)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progres', 'In Progres'),
        ('done', 'Done'),
        ('сanceled', 'Canceled'),
    ], default='scheduled', compute='_compute_state', store=True, tracking=True)
    description = fields.Text(tracking=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_unig', 'unique (name)', """Only one name can be defined for each user!""")
    ]

    # def action_in_progres(self):
    #     return {
    #         'name': _('In Progres %s') % self.name,
    #         'view_mode': 'form',
    #         'res_model': 'rental.wizard.on_rent',
    #         'type': 'ir.actions.act_window',
    #         'target': 'new'
    #     }



    @api.depends('active')
    def _compute_state(self):
        for demo in self:
            if not demo.active:
                demo.state = 'unavailable'
            else:
                demo.state = demo.state
