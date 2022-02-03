from odoo.tests import tagged, Form
from .common import TestIpstack, RETURN_DATA

@tagged('ipstack')
class TestCar(TestIpstack):
    
    def test_onchange(self):
        self.env['ir.config_parameter'].sudo().set_param('ipstack.key', '78fc7fe17f72e5974977cabdf4716e63')
        partner_form = Form(self.partner_1)
        partner_form.ip = '94.176.199.59'
        partner = partner_form.save()
        self.assertEqual(partner.city, RETURN_DATA['city'])
        self.assertEqual(partner.zip, RETURN_DATA['zip'])
        self.assertEqual(partner.country_id.name, RETURN_DATA['country_name'])