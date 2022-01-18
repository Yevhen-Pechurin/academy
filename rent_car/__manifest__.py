# -*- coding: utf-8 -*-
{
    'name': "RentCar",

    'description': """
       Module for Service Stations
    """,
    'author': "Shkvalik",
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'Inventory',
    'version': '15.0',
    'depends': ['base', 'mail'],
    'license': 'GPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}