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

    def test_01_action_garage(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.assertTrue(self.car_1.partner_id, 'Car partner did not take off \nStatus:%s' % self.car_1.partner_id)
        self.car_1.action_garage()
        self.assertEqual(self.car_1.status, 'in_garage', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.assertFalse(self.car_1.partner_id, 'Car partner did not take off \nStatus:%s' % self.car_1.partner_id)
        self.assertTrue(self.car_1.loan_history_ids.end, 'End of car rental not received: %s' % self.car_1.loan_history_ids.end)

    def test_on_loan(self):
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)
        self.car_1.action_loan()
        self.assertEqual(self.car_1.status, 'on_loan', 'Car status is not correct\nStatus:%s' % self.car_1.status)

    def test_get_car_list(self):
        car_list = self.Car.get_car_list('First')
        self.assertEqual(car_list, {'car_list': [{'id': self.car_1.id, 'model': self.car_1.model},
                                                 {'id': self.car_2.id, 'model': self.car_2.model}]},
                         'Car status is not correct\nStatus:%s' % car_list)

    def test_get_car_info(self):
        car_info = self.Car.get_car_info(self.car_1.id)
        self.assertEqual(car_info, [{'id': int(self.car_1.id), 'year': self.car_1.year, 'odometer': 100000, 'model': 'First'}])

    def test_cron_overdue_messages(self):
        result = self.Car._cron_overdue_messages()
        self.assertEqual(result, {}, result)


