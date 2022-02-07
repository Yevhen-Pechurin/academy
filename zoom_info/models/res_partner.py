# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    zoom_api_company_id = fields.Char('Zoom api company Id')  # technical field for frontend
