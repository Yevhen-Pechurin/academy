from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import ValidationError, UserError


class WizardNewDemo(models.TransientModel):
    _name = 'demo.wizard.new_demo'
    _description = 'Wizard New Demo'

    partner_id = fields.Many2one('res.partner')
    date = fields.Date()

    def action_new_demo(self):
        ctx = self._context
        demo = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        date = fields.Datetime().now()
        demo.write({
            'partner_id': self.partner_id.id,
            'date': self.date,
            'status': 'scheduled',
        })

    @api.constrains('date')
    def constrain_date(self):
        if self.date <= fields.Date.today():
            raise ValidationError('Вы не можете выбрать такую дату')