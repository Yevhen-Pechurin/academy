from odoo import models, fields


class WizardOnHand(models.Model):
    _name = "library.wizard.on_hand"
    _description = 'WizardOnHand'

    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()

    def action_wizard_on_hand(self):
        pass

    def action_cancale(self):
        pass
