# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class State(models.Model):
    _name = "demo.state"
    _description = "Demo States"

    name = fields.Char('State Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order states. Lower is better.")
    fold = fields.Boolean('Folded in Pipeline',
                          help='This state is folded in the kanban view when there are no records in that state to display.')


class Demo(models.Model):
    _name = 'demo.demo'
    _inherit = 'mail.thread'
    _description = 'Demo soft'

    name = fields.Char(default='New', readonly=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Salesperson', required=False, default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Client', tracking=True)
    date = fields.Date()
    state_id = fields.Many2one('demo.state', string='State', group_expand='_read_group_state_ids',
                               readonly=False, store=True, tracking=True)
    description = fields.Text(tracking=True)


    @api.model
    def _read_group_state_ids(self, states, domain, order):
        return self.env['demo.state'].search([], order=order)


    # def _compute_state_id(self):
    #     for demo in self:
    #         if not demo.state_id:
    #             demo.state_id = demo._state_find(domain=[('fold', '=', False)]).id


    _sql_constraints = [
        ('name_unig', 'unique (name)', """Only one name can be defined for each demo!""")
    ]


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('demo.demo') or _('New')
        return super(Demo, self).create(vals)


    # state = fields.Selection([
    #     ('scheduled', 'Scheduled'),
    #     ('in_progress', 'In Progress'),
    #     ('done', 'Done'),
    #     ('canceled', 'Canceled'),
    # ], group_expand='_expand_states', store=True, tracking=True)  # default='scheduled',

    # def _expand_states(self, states, domain, order):
    #     return[key for key, val in type(self).state_id.selection]