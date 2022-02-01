from odoo.tests import tagged
from .common import TestCarCommonBase


@tagged('car')
class TestCar(TestCarCommonBase):

    def test_compute_name(self):
        self.assertEqual(self.car_1.name, 'First 31215', 'Car number wrong\nName:%s' % self.car_1.name)

    def test_action_unavailable(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.car_1.action_unavailable()
        self.assertEqual(self.car_1.status, 'unavailable', 'Car status is not correct\nStatus:%s' % self.car_1.status)

    def test_action_repair(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.car_1.action_repair()
        self.assertEqual(self.car_1.status, 'under_repair', 'Car status is not correct\nStatus:%s' % self.car_1.status)

    def test_action_garage(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.assertTrue(self.car_1.partner_id, 'Car partner did not take off \nStatus:%s' % self.car_1.partner_id)
        self.car_1.action_repair()
        self.assertEqual(self.car_1.status, 'under_repair', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.assertFalse(self.car_1.partner_id, 'Car partner did not take off \nStatus:%s' % self.car_1.partner_id)

    def test_on_loan(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.car_1.action_loan()
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)

