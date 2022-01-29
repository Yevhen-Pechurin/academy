from odoo import models, fields

class DemoReport(models.Model):
    _name = 'demo.demo.report'
    _description = 'Demo Report'
    _auto = False

    name = fields.Char()
    salesperson = fields.Char()
    partner_id = fields.Many2one('res.partner')
    date = fields.Date()

    # avg_count = fields.Float(group_operator='avg')
    # max_year = fields.Integer(group_operator='max')


    # @property
    # def _table_query(self):
    #     return """
    #         SELECT
    #         dd.id,
    #         dd.id demo_id,
    #         dd.partner_id,
    #         dd.salesperson,
    #         dd.date,
    #         dd.state
    #         FROM demo_demo dd
    #     """