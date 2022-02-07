# -*- coding: utf-8 -*-
# from odoo import http


# class ZoomInfo(http.Controller):
#     @http.route('/zoom_info/zoom_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoom_info/zoom_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoom_info.listing', {
#             'root': '/zoom_info/zoom_info',
#             'objects': http.request.env['zoom_info.zoom_info'].search([]),
#         })

#     @http.route('/zoom_info/zoom_info/objects/<model("zoom_info.zoom_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoom_info.object', {
#             'object': obj
#         })
