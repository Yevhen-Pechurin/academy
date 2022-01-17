# -*- coding: utf-8 -*-
# from odoo import http


# class RentalCar(http.Controller):
#     @http.route('/rental_car/rental_car', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rental_car/rental_car/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rental_car.listing', {
#             'root': '/rental_car/rental_car',
#             'objects': http.request.env['rental_car.rental_car'].search([]),
#         })

#     @http.route('/rental_car/rental_car/objects/<model("rental_car.rental_car"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rental_car.object', {
#             'object': obj
#         })
