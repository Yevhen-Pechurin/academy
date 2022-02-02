from openupgradelib import openupgrade

_field_adds = [
    ("partner_id", "rental.car", "rental_car", "many2one", False, "odoo15"),
    ("status", "rental.car", "rental_car", "selection", False, "odoo15"),

]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.add_fields(env, _field_adds)
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE library_book
            SET partner_id = client_id,
            status=car_status
            
        """, )
