from odoo.tests.common import TransactionCase, tagged
from datetime import datetime


@tagged('post_install', '-at_install')
class RentalTestCar(TransactionCase):
    @classmethod
    def setUpClass(self):
        super(RentalTestCar, self).setUpClass()
        self.seq_value = self.env['ir.sequence'].next_by_code('rental.car')
        print(self.seq_value)
        self.test_car = self.env['rental.car'].create({
            'model': 'Test',
            'number': 0,
            'year': datetime.now()
        })

        self.test_partner = self.env['res.partner'].create({
            'name': 'Test Test',
        })

        self.test_car.partner_id = self.test_partner.id

        self.test_repair_history = self.env['rental.repair'].create({
            'car_id': self.test_car.id,
            'end': True,
            'end_date': datetime.now()
        })

        self.test_loan_history = self.env['rental.loan'].create({
            'car_id': self.test_car.id,
            'end': False,
            'due_date': datetime.now(),
            'partner_id': self.test_partner.id
        })
