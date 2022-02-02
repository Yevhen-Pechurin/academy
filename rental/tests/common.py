from odoo.addons.base.tests.common import TransactionCase


class TestCarCommonBase(TransactionCase):

    def setUp(self):
        super(TestCarCommonBase, self).setUp()
        self.CarInfo = self.env['rental.car.info']
        self.Car = self.env['rental.car']
        self.Partner = self.env['res.partner']

        self.partner_1 = self.Partner.create({
            'name': 'Test Partner',
        })

        self.car_info_1 = self.CarInfo.create({
            'name': 'Opel',
        })

        # self.env['ir.sequence'].search([
        #     ('code', '=', 'rental.car'),
        # ]).write({
        #     'number_next': 1,
        #     'padding': 6,
        # })

        self.car_1 = self.Car.create({
            'name': 'Opel',
            'number': '75643',
            'car_id': self.car_info_1.id,
            'status': 'on_rent',
            'partner_id': self.partner_1.id
        })

        self.car_2 = self.Car.create({
            'car_id': self.car_info_1.id,
            'status': 'in_garage',
            'partner_id': self.partner_1.id
        })




# -c /home/olga/PycharmProjects/academy/odoo.conf
# --test-enable -d rental_car -i rental_car --log-level=test --stop-after-init --test-tags car --dev=xml