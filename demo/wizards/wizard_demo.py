from odoo import fields, models


class WizardDemo(models.TransientModel):
    _name = 'demo.wizard.demo'

    _description = 'Wizard for user'

    date = fields.Date()

    def demo(self):
        partner = self.env['res.partner'].sudo().browse(self.env.context['active_ids'])
        self.env['demo.demo'].create([{
            'name': 'Demo for %s' % partner.name,
            'user_id': self.env.user.id,
            'partner_id': partner.id,
            'date': self.date
        }])
