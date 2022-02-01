from odoo.tests.common import TransactionCase, tagged
from datetime import datetime


@tagged('post_install', '-at_install')
class RentalTestCar(TransactionCase):

    def setUp(self):
        super(RentalTestCar, self).setUp()

        def patched_sequnce(self):
            seq = self.env['ir.sequence'].search([('name', '=', 'Car')])
            return seq.prefix + str(seq.number_next_actual).zfill(seq.padding)

        self.patch(type(self.env['rental.car']), 'sequence', patched_sequnce)

        self.test_car = self.env['rental.car'].create({
            'model': 'Test',
            'number': 0,
            'year': datetime.now()
        })
        self.test_car_id = self.test_car.id

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
