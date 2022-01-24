from odoo import fields, models


class WizardDemo(models.TransientModel):
    _name = 'demo.wizard.demo'

    _description = 'Wizard for user'

    date = fields.Date()
    partner_id = fields.Many2one('res.partner')

    def demo(self):
        self.env['demo.demo'].sudo().create({
            'name': 'Demo for %s' % (self.partner_id.name),
            'user_id': lambda self: self.env.user.name,
            'partner_id': self.partner_id.id,
            'date': self.date
        })