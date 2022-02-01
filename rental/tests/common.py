from odoo.tests import TransactionCase, SavepointCase


class TestCarCommonBase(SavepointCase):

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
        self.car_1 = self.Car.create({
            'model': 'Model4',
            'year': '2021',
            'status': 'on_loan',
            'odometer': '10000',
            'partner_id': self.partner_1.id,
        })

        self.car_2 = self.Car.create({
            'model': 'Model2222',
            'year': '2019',
            'status': 'in_garage',
            'odometer': '22222',
            'partner_id': self.partner_1.id,
        })

