# -*- coding: utf-8 -*-
# from odoo import http


# class Ipstack(http.Controller):
#     @http.route('/ipstack/ipstack', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ipstack/ipstack/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ipstack.listing', {
#             'root': '/ipstack/ipstack',
#             'objects': http.request.env['ipstack.ipstack'].search([]),
#         })

#     @http.route('/ipstack/ipstack/objects/<model("ipstack.ipstack"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ipstack.object', {
#             'object': obj
#         })
