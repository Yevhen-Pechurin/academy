from dateutil.relativedelta import relativedelta
from odoo import fields
from odoo.addons.base.tests.common import TransactionCase

class TestCarCommonBase(TransactionCase):

    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.Car = self.env['rental.car']
        self.CarManufacturer = self.env['rental.car_manufacturer']
        self.CarModel = self.env['rental.car_model']
        self.CarRentalHistory = self.env['rental.history']
        self.CarMaintenanceHistory = self.env['rental.maintenance_history']
        self.Rentee = self.env['res.partner']

        self.rentee_1 = self.Rentee.create({
            'name': 'Test Profile',
        })

        self.car_manufacturer_1 = self.CarManufacturer.create({
            'name': 'Tesla',
        })

        self.car_model_1 = self.CarModel.create({
            'model_name': 'Model X',
            'manufacturer_id': self.car_manufacturer_1.id,
        })

        """self.car_maintenance_history_1 = self.CarMaintenanceHistory.create({
        
        })"""

        self.car_1 = self.Car.create({
            'model': 'Model X',
            'status': 'on_maintenance',
            'year': 2019,
            'odometer': 7446,
            'client_id': False,
            'date_rented': False,
            'rental_history_ids': False,
        })

        self.car_rental_history_1 = self.CarRentalHistory.create({
            'car_id': self.car_1.id,
            'rentee_id': self.rentee_1.id,
            'date_rented': (fields.Datetime.today() - relativedelta(months=1)).strftime('%Y-%m-%d'),
            'date_returned': (fields.Datetime.today() - relativedelta(days=26)).strftime('%Y-%m-%d'),
            'initial_odometer_value': 7005,
            'final_odometer_value': 7447,
        })

        self.car_1.write({'rental_history_ids': self.car_rental_history_1.ids})