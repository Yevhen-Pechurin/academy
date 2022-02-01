from odoo.addons.base.tests.common import TransactionCase
from odoo.fields import Datetime


class TestCarCommonBase(TransactionCase):
    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.Car = self.env['rental.car']
        self.Partner = self.env['res.partner']
        # self.repair_history = self.env['rental.repair']
        # self.loan_history = self.env['rental.loan']

        self.partner_1 = self.Partner.create({
            'name': 'Test Partner'
        })

        self.car_1 = self.Car.create({
            'number': 31215,
            'model': 'First',
            'year': Datetime.now(),
            'odometer': 100000,
            'status': 'on_loan',
            'partner_id': self.partner_1.id
        })
