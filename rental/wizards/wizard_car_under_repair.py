from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class WizardUnderRepair(models.TransientModel):
    _name = 'rental.wizard.under_repair'
    _description = 'Wizard Under Repair'
    pass

    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()

    def action_under_repair(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        today = fields.Datetime().now()
        car.write({
            'partner_id': self.partner_id.id,
            'due_date': self.due_date,
            'status': 'under_repair',
        })
        self.env['rental.repair_history'].create({
            'car_id': car.id,
            'partner_id': self.partner_id.id,
            'date_under_repair': today,
            'due_date': self.due_date,
        })

    @api.constrains('due_date')
    def constrain_due_date(self):
        if self.due_date <= fields.Date.today():
            raise ValidationError('Вы не можете выбрать такую дату')


