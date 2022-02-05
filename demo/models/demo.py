from odoo import fields, _, api, models
from datetime import timedelta


class Stage(models.Model):
    _name = 'demo.stage'
    _description = 'class for stages'

    name = fields.Char()
    fold = fields.Boolean(default=False)


class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'Class for Demonstrations'
    _inherit = ['mail.thread']

    def _expand_stages(self, *kw):
        return self.env['demo.stage'].search([('name', 'not in', ['Done', 'Canceled'])])

    name = fields.Char(readonly=True, tracking=True, default='New')
    partner_id = fields.Many2one('res.partner', tracking=True)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id, tracking=True)
    description = fields.Text(tracking=True)
    date = fields.Date(default=fields.Date.today(), tracking=True, required=True)
    stage_id = fields.Many2one('demo.stage', group_expand='_expand_stages', tracking=True)

    _sql_constraints = [
        ('name_unig', 'unique (name)', "Record with this name already exists!")
    ]

    @api.model
    def create(self, vals_list):
        vals_list['user_id'] = self.env.user.id
        vals_list['name'] = self.env['ir.sequence'].next_by_code('demo.demo')
        return super(Demo, self).create(vals_list)

    def _cron_delete_old_demoes(self):
        demoes = self.env['demo.demo'].search([])
        for demo in demoes:

            if demo.date + timedelta(days=1) < fields.Date.today():
                demo.unlink()
