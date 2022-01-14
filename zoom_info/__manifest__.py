################################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2019 SmartTek (<https://smartteksas.com/>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

{
    'name': "Zoom Info",
    'summary': """SmartTekSas integration with Zoom Info""",
    'version': '14.0.0.0',
    'category': 'CRM',
    'author': "Smart Tek Solutions and Services",
    'website': "https://smartteksas.com/",
    'depends': [
        'base',
        'web',
        'crm',
    ],
    'data': [
        'views/res_config_settings.xml',
        'views/assets.xml',
        'views/res_partner.xml',
    ],
    'qweb': [
        'static/src/xml/zoom_list.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
