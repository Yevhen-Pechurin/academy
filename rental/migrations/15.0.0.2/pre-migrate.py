from openupgradelib import openupgrade


_field_adds = [
    ("client_id", "rental.car", "rental_car", "many2one", False, "rental"),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.add_fields(env, _field_adds)
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE rental_car
            SET client_id = partner_id
        """,
    )