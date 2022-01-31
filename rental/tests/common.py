from odoo.addons.base.tests.common import TransactionCase

class TestCarCommonBase(TransactionCase):

    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.Car = self.env['rental.car']


        self.car_1 = self.Car.create({
            'model': 'Model X',
            'status': 'on_maintenance',
            'year': 2019,
            'odometer': 7446,
            
        })