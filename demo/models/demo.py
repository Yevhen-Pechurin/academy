# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class State(models.Model):
    _name = "demo.state"
    _description = "Demo States"

    name = fields.Char('State Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order states. Lower is better.")
    is_won = fields.Boolean('Is Won Stage?')
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


    _sql_constraints = [
        ('name_unig', 'unique (name)', """Only one name can be defined for each demo!""")
    ]


    @api.model
    def _read_group_state_ids(self, states, domain, order):
        return self.env['demo.state'].search([], order=order)


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('demo.demo') or _('New')
        return super(Demo, self).create(vals)


    def action_view_my_demos(self):
        self.ensure_one()
        return {
            'name': _('My Demos'),
            'view_mode': 'tree,form',
            'res_model': 'demo.demo',
            'domain': [('user_id', '=', self.id)],
            'type': 'ir.actions.act_window'
            # 'context': {'search_default_client_id': self.id}
        }




    # state = fields.Selection([
    #     ('scheduled', 'Scheduled'),
    #     ('in_progress', 'In Progress'),
    #     ('done', 'Done'),
    #     ('canceled', 'Canceled'),
    # ], group_expand='_expand_states', store=True, tracking=True)  # default='scheduled',

    # def _expand_states(self, states, domain, order):
    #     return[key for key, val in type(self).state_id.selection]