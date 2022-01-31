from .common import RentalTestCar
from odoo.tests import tagged


@tagged('car')
class StartTest(RentalTestCar):
    def test_default_values_car(self):
        self.assertEqual(self.test_car.status, 'in_garage')
        self.assertEqual(self.test_car.active, True)

    def test_compute_car(self):
        self.assertEqual(self.test_car.name, self.test_car.model + str(self.test_car.number))

    def test_sequence_car(self):
        self.assertEqual(self.test_car.code, 'Car00018')

    def test_statuses(self):
        self.test_car.action_unavailable()
        self.assertEqual(self.test_car.status, 'unavailable')
        self.test_car.action_repair()
        self.assertEqual(self.test_car.status,'under_repair')
