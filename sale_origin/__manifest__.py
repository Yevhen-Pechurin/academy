# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Origin',
    'version' : '1.0',
    'category': 'Sale',
    'website': '',
    'depends' : ['base', 'mail', 'website', 'sales_team', 'payment', 'portal', 'utm', 'sale'],

    'data': [
        "security/ir.model.access.csv",

        "views/views.xml",
        "report/sale_report_template.xml",
         ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
