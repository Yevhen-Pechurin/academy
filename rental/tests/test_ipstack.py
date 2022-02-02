from odoo.tests import tagged, Form
from .common import TestIpstack, RETURN_DATA

@tagged('ipstack')
class TestCar(TestIpstack):
    
    def test_onchange(self):
        partner_form = Form(self.partner_1)
        partner_form.ip = '94.176.199.59'
        partner = partner_form.save()
        self.assertEqual(partner.city, RETURN_DATA['city'])
        self.assertEqual(partner.zip, RETURN_DATA['zip'])
        self.assertEqual(partner.countre_id.name, RETURN_DATA['countre_name'])