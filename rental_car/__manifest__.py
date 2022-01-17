# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Rental Car',
    'version' : '1.0',
    'category': 'Car',
    'website': 'https://www.youtube.com/watch?v=tkqef33yRNA&ab_channel=Oxxxymiron-Topic',
    'depends' : ['base', 'mail'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        # 'data/ir_cron.xml',
        "wizards/view_car_for_rent.xml",
        "views/views.xml",

    ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
