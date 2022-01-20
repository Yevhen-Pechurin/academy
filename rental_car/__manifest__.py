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
        "views/views.xml",

    ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    "assets": {
        'web.assets_qweb': [
            'static/src/xml/my_widget.xml',
        ],
        "web.assets_backend": [
            'rental_car/static/src/js/my_widget.js',

        ],

    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
