from odoo import models, fields

class BookReport(models.Model):
    _name = 'library.book.report'
    _description = 'Book Report'
    _auto = False

    book_id = fields.Many2one('library.book')
    client_id = fields.Many2one('res.partner')
    avg_count = fields.Float(group_operator='avg')
    max_year = fields.Integer(group_operator='max')
    author_id = fields.Many2one('library.author')

    @property
    def _table_query(self):
        return """
            SELECT
            lb.id,
            lb.id book_id,
            COALESCE (year, 0) avg_count,
            COALESCE (year, 0) max_year,
            lbi.author_id
            FROM library_book lb
            LEFT JOIN library_book_info lbi ON lb.book_id = lbi.id
        """