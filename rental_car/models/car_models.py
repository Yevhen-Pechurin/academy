from odoo import fields, models, api, _


class Model(models.Model):
    _name = "rental_car.model"
    _description = "Model"

    name = fields.Char(tracking=True)


class Brand(models.Model):
    _name = "rental_car.brand"
    _description = "Car`s Brand"
    _inherit = 'mail.thread'

    name = fields.Char(tracking=True)
    country = fields.Many2one("res.country", tracking=True)
    model_id = fields.Many2one("rental_car.model", tracking=True)
    image = fields.Image(string="Image", max_width=256, max_height=256)
    description = fields.Text(tracking=True)


class RentHistory(models.Model):
    _name = "rental_car.history"
    _description = "History"

    car_id = fields.Many2one("rental_car.car")
    client_id = fields.Many2one("res.partner")
    date_for_rent = fields.Datetime()
    date_in_garage = fields.Datetime()
    odometer_start_value = fields.Integer()
    odometer_end_value = fields.Integer()
    due_date = fields.Datetime()


class RepairHistory(models.Model):
    _name = "rental_car.repair_history"
    _description = "Repair History"

    car_id = fields.Many2one("rental_car.car")
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    repair_description = fields.Char()


class Car(models.Model):
    _name = "rental_car.car"
    _description = "Car"
    _inherit = 'mail.thread'

    brand_id = fields.Many2one("rental_car.brand", tracking=True)
    number = fields.Char(tracking=True)
    description = fields.Text()
    rent_history_id = fields.One2many("rental_car.history", "car_id")
    name = fields.Char(compute='_compute_car_name')
    year_of_manufacture = fields.Integer()
    odometer_value = fields.Integer(tracking=True)
    status = fields.Selection([
        ('in_garage', 'In Garage'),
        ('for_rent', 'For Rent'),
        ('under_repair', 'Under Repair'),
        ('not_available', 'Not Available'),
    ], tracking=True)
    due_date = fields.Datetime()
    client_id = fields.Many2one("res.partner")
    image = fields.Image(string="Image", max_width=256, max_height=256)
    repair_history_id = fields.One2many('rental_car.repair_history', 'car_id')



    _sql_constraints = [
        ('number_unique',
         'unique(number)',
         'Choose another value - it has to be unique!')
    ]


    @api.depends('brand_id', 'number')
    def _compute_car_name(self):
        for record in self:
            record.name = (str(record.brand_id.name) + " " + str(record.number))

    def action_for_rent(self):
        return {
            'name': _('For Rent'),
            'view_mode': 'form',
            'res_model': 'rental_car.car.for_rent',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_in_garage(self):
        return {
            'name': _('In Garage'),
            'view_mode': 'form',
            'res_model': 'rental_car.car.in_garage',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_under_repair(self):
        return {
            'name': _('Under Repair'),
            'view_mode': 'form',
            'res_model': 'rental_car.car.under_repair',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_back_from_repair(self):
        last_history = self.repair_history_id[-1]
        if last_history:
            last_history.write({
                'end_date': fields.Datetime.now()
            })
        self.write({
            'status': 'in_garage',
        })

    # def overdue_notification(self):
    #     today = fields.Datetime.now()
    #     overdue_books = self.env['library.book'].search([
    #         ('status', '=', 'on_hand'),
    #         ('due_date', '<', today),
    #         ('overdue_notification_date', '!=', today)
    #     ])
    #     for book in overdue_books:
    #         body = '%s , термін користуваня книгою %s вийшов. Поверніть, будь ласка, книгу на полицю' % (
    #             book.client_id.name, book.name)
    #         subtype = self.env.ref('mail.mt_comment')
    #         book.message_post(body=body, partner_ids=book.client_id.ids, message_type='comment', subtype_id=subtype.id)
    #         book.write({
    #             'overdue_notification_date': fields.Datetime.now()
    #         })


# class ResPartner(models.Model):
#     _name = 'res.partner'
#     _inherit = 'res.partner'
#
#     books_count = fields.Integer(compute='_compute_books_count')
#
#     def _compute_books_count(self):
#         book_data = self.env['library.book'].read_group(
#             domain=[('client_id', 'in', self.ids)],
#             fields=['client_id'], groupby=['client_id']
#         )
#         self.books_count = 0
#         for group in book_data:
#             partner = self.browse(group['client_id'][0])
#             partner.books_count = group['client_id_count']
#
#     def show_books(self):
#         self.ensure_one()
#         return {
#             'name': _('Client`s Books'),
#             'view_mode': 'tree,form',
#             'res_model': 'library.book',
#             'domain': [('client_id', '=', self.id)],
#             'type': 'ir.actions.act_window',
#         }
