from datetime import timedelta

from odoo import fields
from odoo.tests import TransactionCase, SavepointCase


class TestCarCommonBase(TransactionCase):

    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.Car = self.env['rental.car']
        self.Partner = self.env['res.partner']
        self.partner_1 = self.Partner.create({
            'name': 'Test Partner',
        })
        self.env['ir.sequence'].search([
            ('code', '=', 'rental.car'),
        ]).write({
            'number_next': 1,
            'padding': 6,
        })
        today = fields.Datetime().now()
        self.car_1 = self.Car.create({
            'model': 'Model4',
            'year': '2021',
            'status': 'on_loan',
            'odometer': '10000',
            'client_id': self.partner_1.id,
            'history_ids': [(0, 0, {
                'car_id': 1,
                'partner_id': self.partner_1.id,
                'date_in_garage': today,
                'date_on_loan': fields.Datetime.now() - timedelta(days=10),
            })]
        })

        self.car_2 = self.Car.create({
            'model': 'Model2222',
            'year': '2019',
            'status': 'in_garage',
            'odometer': '22222',
            'client_id': self.partner_1.id,
            'history_ids': [(0, 0, {
                'car_id': 2,
                'partner_id': self.partner_1.id,
                'date_in_garage': today,
                'date_on_loan': fields.Datetime.now() - timedelta(days=10),
            })]
        })

