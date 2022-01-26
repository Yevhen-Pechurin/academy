# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Rental Car',
    'version' : '1.0',
    'category': 'Car',
    'website': 'https://www.youtube.com/watch?v=tkqef33yRNA&ab_channel=Oxxxymiron-Topic',
    'depends' : ['base', 'mail', 'website'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        # 'data/ir_cron.xml',
        "wizards/view_car_for_rent.xml",
        "wizards/view_car_ingarage.xml",
        "wizards/view_car_under_repair.xml",
        "report/car_report.xml",
        "report/qrcode_car_template.xml",
        "report/barcode_car_template.xml",
        "views/views.xml",

    ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    "assets": {
        'web.assets_qweb': [
            # 'rental_car/static/src/my_owl_component/my_owl_component.xml',
            # 'rental_car/static/src/my_owl_component/test.xml',
        ],
        "web.assets_backend": [
            # 'rental_car/static/src/my_owl_component/my_owl_component.js',

        ],

    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
