# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Test Library',
    'description': """Test module <Library> made by Inspiration679""",
    'category': 'Library',
    'website': 'https://github.com/Inspiration679',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/book_view.xml',
        'wizards/wizard_on_hand.xml',
        'data/ir_cron.xml',
        'views/books.xml',
        'views/book.xml',

    ],
    'demo': [
        'demo/library_demo.xml',
    ],
    'web.assets_backend': [
        'library/static/src/js/**/*',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
