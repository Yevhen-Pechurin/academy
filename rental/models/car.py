from odoo import fields, api, models, _


class Car(models.Model):
    _name = 'rental.car'
    _description = 'Class for cars'
    _inherit = ['image.mixin', 'mail.thread']

    name = fields.Char(compute='_compute_name', readonly=True)
    number = fields.Integer(tracking=True)
    model = fields.Char(tracking=True)
    year = fields.Date(tracking=True)
    active = fields.Boolean(string='Active', default=True)
    code = fields.Char(copy=False, readonly=True)
    status = fields.Selection([
        ('in_garage', "In the garage"),
        ('on_loan', 'On Loan'),
        ('under_repair', 'Under repair'),
        ('unavailable', 'Unavailable')

    ], default='in_garage', tracking=True)
    loan_date = fields.Date(tracking=True)
    partner_id = fields.Many2one('res.partner', readonly=True)
    loan_history_ids = fields.One2many('rental.loan', 'car_id')
    repair_history_ids = fields.One2many('rental.repair', 'car_id')
    odometer = fields.Integer(tracking=True)
    @api.depends('number', 'model')
    def _compute_name(self):
        for i in self:
            i.name = str(i.model) + str(i.number)

    def action_loan(self):
        return {
            'name': _('On Loan'),
            'res_model': 'rental.wizard.loan',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new'
        }

    def action_unavailable(self):
        self.sudo().write({'status': 'unavailable'})

    def action_repair(self):
        self.env['rental.repair'].sudo().create({
            'car_id': self.id
        })

        self.sudo().write({'status': 'under_repair'})

    def action_garage(self):

        self.sudo().write({'status': 'in_garage', 'partner_id': False})
        try:
            if self.loan_history_ids[-1]:
                self.sudo().loan_history_ids[-1].end = True
        except IndexError:
            pass

        try:
            if self.repair_history_ids[-1]:
                self.sudo().repair_history_ids[-1].end = True
                self.sudo().repair_history_ids[-1].end_date = fields.Date.today()
        except IndexError:
            pass

    def _cron_overdue_messages(self):
        cars = self.env['rental.car'].search([])
        try:
            for car in cars:
                last_history = car.loan_history_ids[-1]
                if car.status == 'on_loan' and last_history.due_date < fields.Date.today():
                    car.message_post(body=f'{car.partner_id.name} верните машину {car.name}',
                                     partner_ids=car.partner_id.ids, message_type='comment',
                                     subtype_id=self.env.ref('mail.mt_comment').id)
        except IndexError:
            pass

    @api.model
    def get_cars(self, key, field):
        mass_all = []
        mass_model = []

        for i in self.env['rental.car'].search_read([('model', 'like', key), (field, '!=', False)],
                                                    fields=[field, 'id']):
            if i[field] not in mass_model:
                mass_model.append(i[field])
                i['key'] = i.pop(field)
                mass_all.append(i)

        return mass_all

    @api.model
    def get_cars_info(self, id, field):
        return self.env['rental.car'].search_read([('id', '=', id)], fields=[field])

    def print_qrcode(self):
        return self.env['ir.actions.report']._for_xml_id('rental.action_report_car_qrcode')

    def print_barcode(self):
        return self.env['ir.actions.report']._for_xml_id('rental.action_report_car_barcode')
    @api.model
    def create(self, vals_list):
        vals_list['code']=self.env['ir.sequence'].next_by_code('rental.car')
        return super(Car,self).create(vals_list)


class RepairHistory(models.Model):
    _name = 'rental.repair'
    _description = 'Class for cars repair history'

    end = fields.Boolean()
    start_date = fields.Date(default=fields.Date.today(), readonly=True)
    end_date = fields.Date()
    car_id = fields.Many2one('rental.car')


class LoanHistory(models.Model):
    _name = 'rental.loan'
    _description = 'Class for cars loan history'

    end = fields.Boolean()
    partner_id = fields.Many2one('res.partner')
    due_date = fields.Date()
    car_id = fields.Many2one('rental.car')
