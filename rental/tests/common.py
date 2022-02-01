from unittest.mock import patch
from dateutil.relativedelta import relativedelta
from odoo import fields
from odoo.addons.base.tests.common import TransactionCase
from odoo.tests import SavepointCase, Form


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


RETURN_DATA = ''

class TestIpstack(SavepointCase):
    
    def setUp(self):
        super(TestIpstack, self).setUp()
        self.partner_1 = self.env['res.partner'].create({
            'name': 'Tester',
        })
        def _request_ip_data(self, ip):
            return RETURN_DATA
        patcher = patch('odoo.addons.ipstack.models.api.IpstackAPI.request_ip_data', _request_ip_data)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_onchange(self):
        partner_form = Form(self.partner_1)
        partner_form.ip = ''
        partner = partner_form.save()
        self.assertEqual(partner.city, RETURN_DATA['city'])
        self.assertEqual(partner.zip, RETURN_DATA['zip'])
        self.assertEqual(partner.countre_name, RETURN_DATA['countre_name'])
