from odoo import api, SUPERUSER_ID
from odoo.tools.sql import table_exists


def migrate(cr, version):
    if table_exists(cr, 'bluesky_mrp_workorder_component_required_values'):
        cr.execute("""
        UPDATE bluesky_mrp_workorder_component_requirement cr
        SET picked_qty = old_data.picked_qty, returned_qty = old_data.returned_qty,
            rejected_qty = old_data.rejected_qty, sent_to_client_qty = old_data.sent_to_client_qty,
            variance_qty = old_data.variance_qty
        FROM bluesky_mrp_workorder_component_required_values old_data
        WHERE old_data.mo_id = cr.mo_id AND old_data.product_id = cr.product_id AND old_data.uom_id = cr.uom_id
        """)
        cr.execute("""DROP TABLE bluesky_mrp_workorder_component_required_values CASCADE""")
