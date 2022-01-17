from odoo import http


class Library(http.Controller):

    @http.route("/library/books/", auth='public', website=True)
    def index(self, **kw):
        return http.request.render('library.books_list', {
            'root': '/library',
            'books': http.request.env['library.book'].search([]),
        })

    @http.route('/library/book/<model("library.book"):book>', auth='public', website=True)
    def book(self, book, **kw):
        return http.request.render('library.book', {'book': book})
