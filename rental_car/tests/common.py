
from odoo.tests import HttpCase, tagged, TransactionCase, common

# This test should only be executed after all modules have been installed.
@tagged('rental_car')
class RentalCarTests(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(RentalCarTests, cls).setUpClass()


        cls.brand_1 = cls.env['rental_car.brand'].create({
            'name': 'BMV',
        })

        cls.model_1 = cls.env['rental_car.model'].create({
            'name': 'M5',
            'year_of_manufacture': '2010',
        })

        cls.car_1 = cls.env['rental_car.car'].create({
            'brand_id': cls.brand_1.id,
            'model_id': cls.model_1.id,
            'odometer_value': 200,
            'status': 'in_garage',
        })

        cls.car_2 = cls.env['rental_car.car'].create({
            'brand_id': cls.brand_1.id,
            'model_id': cls.model_1.id,
            'odometer_value': 200,
            'status': 'for_rent',
        })

