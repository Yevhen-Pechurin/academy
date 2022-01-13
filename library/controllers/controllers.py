# -*- coding: utf-8 -*-
from odoo import http


class Library(http.Controller):

    @http.route('/library/library', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/library/books', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('library.listing', {
            'root': '/library',
            'objects': http.request.env['library.book'].sudo().search([]),
        })

    @http.route('/library/book/<model("library.book"):obj>', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('library.object', {
            'object': http.request.env['library.book'].sudo().browse(obj.id)
        })
