from odoo import fields, models


class WizardLoan(models.TransientModel):
    _name = 'rental.wizard.loan'

    _description = 'Wizard for cars loan'

    due_date = fields.Date()
    partner_id = fields.Many2one('res.partner')

    def on_loan(self):
        ctx = self.env.context
        print(self.env.context)
        car = self.env['rental.car'].sudo().search([('id', '=', ctx['active_id'])])
        car.write({'partner_id': self.partner_id.id, 'status': 'on_loan'})
        self.env['rental.loan'].sudo().create({
            'due_date': self.due_date,
            'partner_id': self.partner_id.id,
            'car_id': car.id
        })
