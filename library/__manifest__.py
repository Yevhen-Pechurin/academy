# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Library',
    'version' : '1.0',
    'category': 'Library',
    'website': 'https://www.youtube.com/watch?v=tkqef33yRNA&ab_channel=Oxxxymiron-Topic',
    'depends' : ['mail'],
    'data': [
        "security/ir.model.access.csv",
        'data/ir_cron.xml',
        "wizards/view_book_on_hand.xml",
        "views/views.xml",
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
