# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Origin',
    'version': '1.0',
    'summary': 'Test sale origin',
    'description': """Test module <Sale Origin> made by Inspiration679""",
    'category': 'Product',
    'website': 'https://github.com/Inspiration679',
    'depends': ['base','sale'],
    'data': [
        'views/sale_order_view.xml',
        'reports/report.xml'
    ],
    'demo': [
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}