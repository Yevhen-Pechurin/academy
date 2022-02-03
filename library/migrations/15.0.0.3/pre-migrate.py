from openupgradelib import openupgrade
from odoo.tools.sql import table_exists

_field_adds = [
    ("client_id", "library.history", "library_history", "many2one", False, "library"),
]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.add_fields(env, _field_adds)
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE library_history
            SET client_id = partner_id
        """,
    )
