from odoo import fields, models


class WizardDemo(models.TransientModel):
    _name = 'demo.wizard.demo'

    _description = 'Wizard for creating demoes in contatcs'

    date = fields.Date(required=True)

    def demo_create(self):
        ctx = self.env.context
        partner = self.env['res.partner'].sudo().search([('id', '=', ctx['active_id'])])
        self.env['demo.demo'].create({
            'partner_id': partner.id,
            'date': self.date
        })
