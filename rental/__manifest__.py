# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Rental',
    'version': '1.0',
    'summary': 'Test Car Rental',
    'description': """Test module <Car Rental> made by Inspiration679""",
    'category': 'Cars',
    'website': 'https://github.com/Inspiration679',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/car_rental_view.xml',
        'wizards/wizard_loan.xml',
        'data/ir_cron.xml',
        'report/qrcode.xml',
        'report/qrcode_template.xml',
        'report/barcode.xml',
        'report/barcode_template.xml'

    ],
    'demo': [
        'demo/car_rental_demo.xml',
    ],
    "assets": {
        "web.assets_backend": [

            'rental/static/src/js/list.js',
            'rental/static/src/css/list.css',
            'rental/static/src/js/components/list_widget/list.js'
        ],
        'web.assets_qweb': [

            'rental/static/src/xml/list.xml',
            'rental/static/src/js/components/list_widget/list.xml'
        ],
    },


    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
