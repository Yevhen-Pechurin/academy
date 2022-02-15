from odoo import api, SUPERUSER_ID
from odoo.tools.sql import column_exists


def migrate(cr, version):
    if not column_exists(cr, 'stock_move', 'picked_qty'):
        return
    # save old_data
    cr.execute("""
    CREATE TABLE IF NOT EXISTS bluesky_mrp_workorder_component_required_values (
        mo_id int4,
        product_id int4,
        uom_id int4,
        picked_qty double precision,
        returned_qty double precision,
        rejected_qty double precision,
        sent_to_client_qty double precision,
        variance_qty double precision
    );
    """)
    cr.execute("""
    INSERT INTO bluesky_mrp_workorder_component_required_values (
        mo_id, product_id, uom_id, picked_qty, returned_qty,
        rejected_qty, sent_to_client_qty, variance_qty
    )
    SELECT raw_material_production_id as mo_id, product_id, product_uom as uom_id,
        SUM(picked_qty), SUM(returned_qty), SUM(rejected_qty), SUM(sent_to_client_qty), SUM(variance_qty)
    FROM stock_move
    WHERE raw_material_production_id IS NOT NULL
    GROUP BY raw_material_production_id, product_id, product_uom
    """)
