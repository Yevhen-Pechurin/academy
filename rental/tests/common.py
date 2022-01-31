from odoo.addons.base.tests.common import TransactionCase


class TestCarCommonBase(TransactionCase):

    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.Car = self.env['rental.car']
        self.Partner = self.env['res.partner']
        self.partner_1 = self.Partner.create({
            'name': 'Test Partner',
        })
        self.car_1 = self.Car.create({
            'model': 'Model4',
            'year': '2021',
            'status': 'on_loan',
            'odometer': '10000',
            'partner_id': self.partner_1.id,
        })
