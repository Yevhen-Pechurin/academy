from odoo.tests import SavepointCase, Form
from odoo.addons.ipstack.models.api import IpstackApi

RETURN_DATA = {
    'ip': '94.176.199.59',
    'type': 'ipv4',
    'continent_code': 'EU',
    'continent_name': 'Europe',
    'country_code': 'UA',
    'country_name': 'Ukraine',
    'region_code': '30',
    'region_name': 'Kyiv City',
    'city': 'Kyiv', 'zip': '04119', 'latitude': 50.43333053588867, 'longitude': 30.51667022705078,
    'location': {'geoname_id': 703448, 'capital': 'Kyiv', 'languages': [{'code': 'uk', 'name': 'Ukrainian', 'native': 'Українська'}], 'country_flag': 'https://assets.ipstack.com/flags/ua.svg',
                 'country_flag_emoji': '🇺🇦', 'country_flag_emoji_unicode': 'U+1F1FA U+1F1E6', 'calling_code': '380', 'is_eu': False}}


class TestIpstack(SavepointCase):

    def setUp(self):
        super(TestIpstack, self).setUp()
        self.partner_1 = self.env['res.partner'].create({
            'name': 'Test Partner'
        })

        def _get_ip_data(self, ip):
            return RETURN_DATA
        self.patch(IpstackApi, 'get_ip_data', _get_ip_data)

    def test_onchange(self):
        partner_form = Form(self.partner_1)
        partner_form.ip = '94.176.199.59'
        partner = partner_form.save()
        self.assertEqual(partner.city, RETURN_DATA['city'])
        self.assertEqual(partner.zip, RETURN_DATA['zip'])
        self.assertEqual(partner.country_id.name, RETURN_DATA['country_name'])
