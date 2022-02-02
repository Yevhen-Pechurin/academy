from openupgradelib import openupgrade

_field_adds = [
    ("client_id", "rental.car", "library_car", "many2one", False, "odoo15"),
    ("car_status", "rental.car", "library_car", "selection", False, "odoo15"),

]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.add_fields(env, _field_adds)
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE library_book
            SET client_id = partner_id,
            car_status=status
            
        """, )
