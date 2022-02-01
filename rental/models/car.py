from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CarManufacturer(models.Model):
    _name = 'rental.car.manufacturer'
    _description = 'Car manufacturer'

    name = fields.Char(required=True)
    logo = fields.Image(string="Manufacturer logo", max_width=256, max_height=256)


class CarModel(models.Model):
    _name = 'rental.car.model'
    _description = 'Car model'
    _inherit = 'mail.thread'
    
    model_name = fields.Char(required=True)
    manufacturer_id = fields.Many2one('rental.car.manufacturer', required=True)
    manufacturer_logo = fields.Image(related='manufacturer_id.logo')
    #car_ids = fields.One2many('rental.car', 'model_id')

    _sql_constraints = [
        ('unique_model_name', 'UNIQUE(model_name, manufacturer_id)', """Such a model for this manufacturer already exists!"""),
    ]


class CarRentalHistory(models.Model):
    _name = 'rental.history'
    _description = 'Car rental history'

    car_id = fields.Many2one('rental.car', required=True)
    date_rented = fields.Datetime(default=fields.Datetime.now)
    rentee_id = fields.Many2one('res.partner')
    date_returned = fields.Datetime()
    initial_odometer_value = fields.Integer(default=lambda self: self.car_id.odometer)
    final_odometer_value = fields.Integer()

    @api.constrains('final_odometer_value')
    def check_final_odometer_value(self):
        if self.final_odometer_value and self.initial_odometer_value > self.final_odometer_value:
            raise ValidationError('Invalid input: odometer value after rental cannot be smaller than before rental.')


class CarMaintananceHistory(models.Model):
    _name = 'rental.maintenance.history'
    _description = 'Car maintenance history'


class Car(models.Model):
    _name = 'rental.car'
    _description = 'A car'
    _inherit = 'mail.thread'

    name = fields.Char(compute='_compute_car_name')
    model = fields.Char(required=True) #model_id = fields.Many2one('rental.car.model', required=True)
    number = fields.Char(required=True, default='New', readonly=True)
    logo = fields.Image()    #related='model_id.manufacturer_logo')
    year = fields.Integer()
    status = fields.Selection([
        ('in_garage', 'In garage'),
        ('rented', 'Rented'),
        ('on_maintenance', 'On maintenance'),
        ('unavailable', 'Unavailable'),
        ], default= 'in_garage', required=True, tracking=True)
    date_rented = fields.Datetime()
    client_id = fields.Many2one('res.partner', copy=False)
    odometer = fields.Integer(tracking=True)
    active = fields.Boolean(default=True)
    rental_history_ids = fields.One2many('rental.history', 'car_id')

    _sql_constraints = [
        ('unique_number', 'UNIQUE(number)', """Number is unique for every car!"""),
    ]

    @api.model
    def get_model(self, model_name):
        #Some ways of managing the data:
        """values = {'models': self.env['rental.car.model'].sudo().search([('model_name', 'ilike', model_name)]).read(['id', 'model_name'])}
        """
        """values = {'models': self.env['rental.car'].sudo().search_read([('model_name', 'ilike', model_name)], fields = ['model_name', 'id'], limit=5)}
        """
        """records = self.env['rental.car.model'].sudo().search([('model_name', 'ilike', model_name)])
        #values['models'] = [[r.id, r.model_name] for r in records]
        """
        return self.env['rental.car.model'].sudo().search([('model_name', 'ilike', model_name)]).read(['id', 'model_name'])

    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('rental.car') or _('New')
        return super(Car, self).create(vals)

    @api.depends('model', 'number')
    def _compute_car_name(self):
        for car in self:
            car.name = f'{car.model}_{car.number}'

    @api.onchange('status')
    def onchange_status_rented(self):
        if self.status == 'rented':
            if not self.date_rented:
                self.date_rented = fields.Datetime.now()
        else:
            self.date_rented = False

    @api.depends('active')
    def _compute_status(self):
        for car in self:
            if not car.active:
                car.status = 'unavailable'
            else:
                car.status = 'in_garage'

    def print_barcode(self):
        return self.env['ir.actions.report']._for_xml_id("rental.action_report_car_barcode")