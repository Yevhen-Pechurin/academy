# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class WizardToRent(models.Model):
    _name = 'rental_car.wizard.to_rent'
    _description = 'To Rent'

    partner_id = fields.Many2one('res.partner', requirement=True)
    due_date = fields.Datetime()
    odometr = fields.Integer()

    def action_wizard_to_rent(self):
        ctx = self._context
        car = self.env[ctx['active_model']].sudo().browse(ctx['active_ids'])
        car.write({
            'partner_id': self.partner_id.id,
            'odometr': self.odometr,
            'status': 'in_rent',
            'partner_id': self.partner_id.id
        })
        today = fields.Datetime().now()
        self.env['rental_car.history'].create({
            'car_id': car.id,
            'partner_id': self.partner_id.id,
            'date_to_rent': today,
            'odometr': self.odometr,
            # 'due_date': self.due_date,
            })

    def action_cancel(self):
        pass

    @api.constrains("partner_id")
    def constrain_partner_id(self):
        if self.partner_id:
            raise ValidationError("Нужно указать Уважаемого")