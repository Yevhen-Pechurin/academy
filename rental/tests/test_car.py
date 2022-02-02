from psycopg2.errors import UniqueViolation
from odoo.tests import tagged, HttpCase, Form
from odoo.tools import mute_logger
from .common import TestRentalCommonBase

@tagged('car')
class TestCar(TestRentalCommonBase):

    def test_01_sequence(self):
        self.assertEqual(self.car_1.number, '#000001')
        self.assertEqual(self.car_2.number, '#000002')


@tagged('car')
class TestCarModel(TestRentalCommonBase):

    def test_01_model_name_constraint(self):
        with self.assertRaises(UniqueViolation), mute_logger('odoo.sql_db'):
            self.CarModel.create({
                'model_name': 'Model X',
                'manufacturer_id': self.car_manufacturer_1.id,
            })


@tagged('car')
class TestRentalJs(HttpCase):

    def test_tour(self):
        self.start_tour("/web", 'rental_tour', login='admin', timeout=180)
