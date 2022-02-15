from odoo import api, fields, models


class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    # Control tab
    customer_id = fields.Many2one(
        'res.partner',
        string="Customer",
        domain="[('is_company', '=', True)]",
    )
    customer_no = fields.Char(
        "Customer Order No.",
    )
    sale_order_id = fields.Many2one(
        'sale.order',
        "Sales Order",
    )
    order_fulfilment = fields.Selection([
        ('full', 'Full'),
    ], string="Order Fulfilment", default='full')  # TODO: need value to selection
    min_order_qty = fields.Integer(
        "Min.Order Qty:",
    )
    batch_code_id = fields.Many2one(
        "stock.production.lot",
        "Batch Code",
        copy=False,
    )
    bulk_required = fields.Float(
        "Bulk Required(kg)",
    )
    ppe_required_ids = fields.Many2many(
        "bluesky_mrp_workorder.ppe",
        string="PPE Required",
    )
    bulk_released_by_sign = fields.Binary(
        "Bulk Released By",
        attachment=True,
        copy=False,
    )
    bulk_approved_by_sign = fields.Binary(
        "Bulk Approved By",
        attachment=True,
        copy=False,
    )
    samples_retained_sign = fields.Binary(
        "Samples Retained",
        attachment=True,
        copy=False,
    )

    # Bulk Handover tab
    bulk_received = fields.Float(
        "Bulk Received(g)",
    )
    approved_fill_weight = fields.Float(
        "Approved Fill Weight(g)",
    )
    projected_yield = fields.Float(
        "Projected Yield(Units)",
        compute="_compute_projected_yield",
        store=True,
    )
    min_no_of_units_required = fields.Float(
        "Min.No.of Units Required",
        compute="_compute_projected_yield",
        store=True,
        help="This field will show a  90% value of projected yield units.",
    )
    mixing_sign = fields.Binary(
        "Mixing",
        attachment=True,
        copy=False,
    )
    production_sign = fields.Binary(
        "Production",
        attachment=True,
        copy=False,
    )

    # Component Requirements tab
    component_requirement_ids = fields.One2many(
        'bluesky_mrp_workorder.component_requirement',
        'mo_id',
        "Component Requirements",
        readonly=False,
        compute="_compute_component_requirements",
    )

    # Line Instructions tab
    line_instructions = fields.Text(
        "Line Instructions:",
        copy=True,
    )
    special_instructions = fields.Text(
        "Special Instructions:",
        copy=False
    )

    # Labeling & Coding Requirements tab
    coding_requirements = fields.Text("Coding Requirements")
    image_1st = fields.Image("1st Image")
    image_2nd = fields.Image("2nd Image")
    image_3rd = fields.Image("3rd Image")
    image_4th = fields.Image("4th Image")
    image_5th = fields.Image("5th Image")
    image_6th = fields.Image("6th Image")
    image_7th = fields.Image("7th Image")
    image_8th = fields.Image("8th Image")
    image_9th = fields.Image("9th Image")
    image_10th = fields.Image("10th Image")
    sign_1st = fields.Binary(
        "1st Sign",
        attachment=True,
        copy=False,
    )
    sign_2nd = fields.Binary(
        "2nd Sign",
        attachment=True,
        copy=False,
    )
    sign_3rd = fields.Binary(
        "3rd Sign",
        attachment=True,
        copy=False,
    )
    sign_4th = fields.Binary(
        "4th Sign",
        attachment=True,
        copy=False,
    )
    sign_5th = fields.Binary(
        "5th Sign",
        attachment=True,
        copy=False,
    )
    sign_6th = fields.Binary(
        "6th Sign",
        attachment=True,
        copy=False,
    )
    sign_7th = fields.Binary(
        "7th Sign",
        attachment=True,
        copy=False,
    )
    sign_8th = fields.Binary(
        "8th Sign",
        attachment=True,
        copy=False,
    )
    sign_9th = fields.Binary(
        "9th Sign",
        attachment=True,
        copy=False,
    )
    sign_10th = fields.Binary(
        "10th Sign",
        attachment=True,
        copy=False,
    )

    # Packing & Palletising Instructions tab
    units_per_shipper = fields.Integer(
        "Units Per Shipper",
    )
    shippers_per_layer = fields.Integer(
        "Shippers Per Layer",
    )
    max_layers_per_pallet = fields.Integer(
        "Max. Layers Per Pallet",
    )
    max_units_per_pallet = fields.Integer(
        "Max. Units Per Pallet",
    )
    pallet_requirements = fields.Text(
        "Pallet Requirements",
    )
    special_label = fields.Image(
        "Special Label",
    )

    # First Off Line Production Sample tab
    image_1st_sample = fields.Image("1st Image Sample")
    image_2nd_sample = fields.Image("2nd Image Sample")
    image_3rd_sample = fields.Image("3rd Image Sample")
    image_4th_sample = fields.Image("4th Image Sample")
    image_5th_sample = fields.Image("5th Image Sample")
    sign_1st_sample = fields.Binary(
        "1st Sign Sample",
        attachment=True,
        copy=False,
    )
    sign_2nd_sample = fields.Binary(
        "2nd Sign Sample",
        attachment=True,
        copy=False,
    )
    sign_3rd_sample = fields.Binary(
        "3rd Sign Sample",
        attachment=True,
        copy=False,
    )
    sign_4th_sample = fields.Binary(
        "4th Sign Sample",
        attachment=True,
        copy=False,
    )
    sign_5th_sample = fields.Binary(
        "5th Sign Sample",
        attachment=True,
        copy=False,
    )

    # Bulk Reconciliation tab
    amount_of_bulk_manufactured = fields.Float(
        "Amount of Bulk Manufactured",
    )
    amount_of_bulk_returned = fields.Float(
        "Amount of Bulk Returned",
    )
    avg_fill_weight = fields.Float(
        "Average Fill Weight",
    )
    units_filled_incl_rejects = fields.Integer(
        "Units Filled incl. Rejects",
    )
    total_weight_filled = fields.Float(
        "Total Weight Filled",
        compute="_compute_total_weight_filled",
        store=True,
    )
    amount_of_bulk_wasted = fields.Float(
        "Amount of Bulk Wasted",
        compute="_compute_amount_of_bulk_wasted",
        store=True,
    )
    bulk_yield = fields.Float(
        "Bulk Yield",
        compute="_compute_bulk_yield",
        store=True,
    )

    @api.depends('move_raw_ids.product_id', 'move_raw_ids.product_uom')
    def _compute_component_requirements(self):
        ComponentRequirement = self.env['bluesky_mrp_workorder.component_requirement']
        exist_component_requirements = self.env['bluesky_mrp_workorder.component_requirement'].search([
            ('mo_id', 'in', self.ids),
        ])
        new_keys = self._get_raw_moves_requirements_key()
        exist_keys = {
            (comp_req.mo_id, comp_req.product_id, comp_req.uom_id): comp_req
            for comp_req in exist_component_requirements
        }
        new_keys_set = set(new_keys)
        exist_keys_set = set(exist_keys)
        for mo in self:
            component_requirements = exist_component_requirements.filtered(lambda x: x.mo_id == mo)
            exist_component_requirements -= component_requirements
            for to_remove_key in exist_keys_set - new_keys_set:
                component_requirements -= exist_keys[to_remove_key]
            vals_list = [{
                'mo_id': to_create_key[0].id,
                'product_id': to_create_key[1].id,
                'uom_id': to_create_key[2].id,
            } for to_create_key in new_keys_set - exist_keys_set]
            if vals_list:
                component_requirements += ComponentRequirement.create(vals_list)
            mo.component_requirement_ids = component_requirements

    @api.depends('move_finished_ids.move_line_ids.lot_id')
    def _compute_batch_code_id(self):
        for mo in self:
            if mo.product_id.tracking != 'lot':
                mo.batch_code_id = False
                continue
            lots = mo.move_finished_ids.move_line_ids.lot_id
            if len(lots) != 1:
                mo.batch_code_id = False
            else:
                mo.batch_code_id = lots

    @api.depends('bulk_received', 'approved_fill_weight')
    def _compute_projected_yield(self):
        for mo in self:
            if not mo.approved_fill_weight:
                projected_yield = 0.0
            else:
                projected_yield = mo.bulk_received / (mo.approved_fill_weight or 1.0)
            mo.projected_yield = projected_yield
            mo.min_no_of_units_required = projected_yield * 0.9

    @api.depends('avg_fill_weight', 'units_filled_incl_rejects')
    def _compute_total_weight_filled(self):
        for mo in self:
            mo.total_weight_filled = mo.avg_fill_weight * mo.units_filled_incl_rejects

    @api.depends('amount_of_bulk_manufactured', 'amount_of_bulk_returned', 'total_weight_filled')
    def _compute_amount_of_bulk_wasted(self):
        for mo in self:
            mo.amount_of_bulk_wasted = mo.amount_of_bulk_manufactured - mo.amount_of_bulk_returned - mo.total_weight_filled

    @api.depends('amount_of_bulk_manufactured', 'amount_of_bulk_returned', 'total_weight_filled')
    def _compute_bulk_yield(self):
        for mo in self:
            if not mo.amount_of_bulk_manufactured:
                mo.bulk_yield = 0.0
            else:
                mo.bulk_yield = (mo.total_weight_filled + mo.amount_of_bulk_returned) * 100 / mo.amount_of_bulk_manufactured

    @api.model_create_multi
    def create(self, vals_list):
        res = super(MRPProduction, self).create(vals_list)
        for mo, vals in zip(res, vals_list):
             mo._log_sign(vals)
        return res

    def write(self, vals):
        res = super(MRPProduction, self).write(vals)
        self._log_sign(vals)
        return res

    def _log_sign(self, vals):
        tracked_fields = [
            'bulk_released_by_sign',
            'bulk_approved_by_sign',
            'samples_retained_sign',
            'mixing_sign',
            'production_sign',
            'sign_1st',
            'sign_2nd',
            'sign_3rd',
            'sign_1st_sample',
            'sign_2nd_sample',
            'sign_3rd_sample',
        ] + ['sign_%dth' % i for i in range(4, 11)] + ['sign_%dth_sample' % i for i in range(4, 6)]
        changed_fields = [
            self._fields[f_name].string
            for f_name, f_value in vals.items()
            if f_value and f_name in tracked_fields and f_name in self._fields
        ]
        if changed_fields:
            self.message_post(
                body="%s signed the field(s):<br/>%s" % (self.env.user.display_name, ', '.join(changed_fields)),
                subtype_id=self.env.ref('mail.mt_note').id,
            )

    def _get_raw_moves_requirements_key(self):
        res = {}
        for move in self.move_raw_ids._origin:
            key = (move.raw_material_production_id, move.product_id, move.product_uom)
            res.setdefault(key, move)
            res[key] |= move
        return res
