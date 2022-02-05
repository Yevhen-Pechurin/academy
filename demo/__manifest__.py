# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'demo',
    'version': '1.0',
    'summary': 'Test demo',
    'description': """Test module <Demo> made by Inspiration679""",
    'category': 'Games',
    'website': 'https://github.com/Inspiration679',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_view.xml',

        'views/menues.xml',
        'data/ir_sequence_demo_name.xml',
        'data/demo_stage_data.xml',
        'wizards/wizard_demo.xml',
        'data/ir_cron_old_demoes.xml'

    ],
    'demo': ['demo/demo_demo.xml'


    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
