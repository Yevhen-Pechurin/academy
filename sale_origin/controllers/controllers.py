# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrigin(http.Controller):
#     @http.route('/sale_origin/sale_origin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_origin/sale_origin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_origin.listing', {
#             'root': '/sale_origin/sale_origin',
#             'objects': http.request.env['sale_origin.sale_origin'].search([]),
#         })

#     @http.route('/sale_origin/sale_origin/objects/<model("sale_origin.sale_origin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_origin.object', {
#             'object': obj
#         })
