# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Demo',
    'version' : '1.0',
    'category': 'Demo',
    'website': 'https://www.youtube.com/watch?v=D1I1x2pYMK0&list=RDD1I1x2pYMK0&start_radio=1&ab_channel=Eminem-Topic',
    'depends' : ['base', 'mail'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "wizards/view_new_demo.xml",
        "views/views.xml",
        "data/demo_statuses.xml",
        "data/ir_sequence.xml",
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
