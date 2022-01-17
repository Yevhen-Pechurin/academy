# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Library',
    'version' : '1.0',
    'category': 'Library',
    'website': 'https://www.youtube.com/watch?v=tkqef33yRNA&ab_channel=Oxxxymiron-Topic',
    'depends' : ['base', 'mail', 'website'],
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        'data/ir_cron.xml',
        "wizards/view_book_on_hand.xml",
        "views/views.xml",
        "views/books_template.xml",
        "views/book_info_template.xml",

    ],
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
