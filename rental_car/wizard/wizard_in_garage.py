from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError

class WizardInGarage(models.Model):
    _name = 'rental_car.wizard.in_garage'
    _description = 'In Garage'

    partner_id = fields.Many2one('res.partner')
    date_to_rent = fields.Datetime(tracking=True)
    due_date = fields.Datetime(tracking=True)
    date_to_return = fields.Datetime(tracking=True)
    odometr_end = fields.Char()

    def action_wizard_in_garage(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        xxx = self.id
        last_history = car.history_ids[-1]
        car.write({
            "status": 'available',
            'odometr': self.odometr_end,
            'partner_id': False,
        })
        today = fields.Datetime().now()
        # history = self.env['rental_car.history'].sudo().browse(last_history)
        # history = self.env['rental_car.history'].sudo().browse(ctx['active_ids'][-1])
        # history = self.env['rental_car.history'].sudo().search([('id', '=', last_history)])
        # print(history,'<<<<<<<<<<<<<<<<<<<<<<<<')
        # history.write({
        last_history.write({
            'odometr_end': self.odometr_end,
            'date_to_return': today,
        })

    def action_cancel(self):
        pass

    # @api.constrains("date_to_return")
    # def constrain_date_to_return(self):
    #     if self.date_to_return < fields.Datetime.now():
    #         raise ValidationError("неверная дата")


