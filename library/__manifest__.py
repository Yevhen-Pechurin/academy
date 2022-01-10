# -*- coding: utf-8 -*-
{
    'name': "Library",

    'description': """
       Module for searching books
    """,
    'author': "Shkvalik",
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'Inventory',
    'version': '15.0',
    'depends': ['base', 'mail'],
    'license': 'GPL-3',
    'data': [
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'wizards/view_wizard_book_on_hand.xml',
        'views/views.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
