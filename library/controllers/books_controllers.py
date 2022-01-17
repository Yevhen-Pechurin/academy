from odoo import http


class BookController(http.Controller):

    @http.route('/library/books/', auth='public', website=True)
    def books(self, **kw):
        books = http.request.env['library.book'].search([])
        return http.request.render('library.books', {'books': books})

    @http.route('/library/<model("library.book"):book>', auth='public', website=True)
    def book(self, book):
        return http.request.render('library.book', {'book': book})
