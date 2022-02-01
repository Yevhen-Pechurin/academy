from odoo.addons.base.tests.common import TransactionCase
from odoo.fields import Datetime


class TestCarCommonBase(TransactionCase):
    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.car = self.env['rental.car']
        # self.repair_history = self.env['rental.repair']
        # self.loan_history = self.env['rental.loan']

        self.car_1 = self.car.create({
            'number': 31215,
            'model': 'First',
            'year': Datetime.now(),
            'odometer': 100000,
            'status': 'on_loan',
            'partner_id': 'base.res_partner_1'
        })
