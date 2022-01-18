# -*- coding: utf-8 -*-
# from odoo import http


# class RentCar(http.Controller):
#     @http.route('/rent_car/rent_car', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rent_car/rent_car/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rent_car.listing', {
#             'root': '/rent_car/rent_car',
#             'objects': http.request.env['rent_car.rent_car'].search([]),
#         })

#     @http.route('/rent_car/rent_car/objects/<model("rent_car.rent_car"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rent_car.object', {
#             'object': obj
#         })
