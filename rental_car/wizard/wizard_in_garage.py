from odoo import models, fields, api


class WizardInGarage(models.Model):
    _name = 'rental_car.wizard.in_garage'
    _description = 'In Garage'

    partner_id = fields.Many2one('res.partner')
    date_to_rent = fields.Datetime(tracking=True).today()
    due_date = fields.Datetime(tracking=True)
    date_to_return = fields.Datetime(tracking=True)

    def action_wizard_in_garage(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])

        today = fields.Date().today()


    def action_cancel(self):
        pass
