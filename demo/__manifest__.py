# -*- coding: utf-8 -*-
{
    'name': "User Story",

    'description': """
       Module for show bonus
    """,
    'author': "Shkvalik",
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'DemoSoft',
    'version': '15.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizards/wizard_demo.xml',
        'data/ir_sequence_data.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
