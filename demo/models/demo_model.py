from odoo import fields, models, api, _

class Status(models.Model):
    _name = "demo.status"
    _description = "Demo"

    name = fields.Char(required=True, tracking=True)


class Demo(models.Model):
    _name = "demo.demo"
    _description = "Demo"
    _inherit = 'mail.thread'

    name = fields.Char(tracking=True, required=True, copy=False, readonly=True, default="Demo")
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Client', tracking=True)
    date = fields.Date(tracking=True)
    status_id = fields.Many2one("demo.status", tracking=True, required=True, default=2)
    description = fields.Text(tracking=True)

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]

    @api.model
    def create(self, vals):
        if vals.get('name', _('Demo')) == _('Demo'):
            vals['name'] = self.env['ir.sequence'].next_by_code('demo.demo') or _('Demo')
            return super(Demo, self).create(vals)


    def action_sheduled(self):
        self.status_id = 1