from odoo import fields, _, api, models


class Stage(models.Model):
    _name = 'demo.stage'
    _description = 'class for stages'

    name = fields.Char()
    fold = fields.Boolean(default=False)

class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'Class for Demonstrations'

    name = fields.Char(readonly=True)
    partner_id = fields.Many2one('res.partner')
    user_id = fields.Many2one('res.users', readonly=True)
    description = fields.Text()
    date = fields.Date(default=fields.Date.today())
    stage_id = fields.Many2one('demo.stage')

    _sql_constraints = [
        ('name_unig', 'unique (name)', "Record with this name already exists!")
    ]

    @api.model
    def create(self, vals_list):
        vals_list['user_id'] = self.env.user.id
        vals_list['name'] = self.env['ir.sequence'].next_by_code('demo.demo')
        return super(Demo, self).create(vals_list)
