from openupgradelib import openupgrade


_field_adds = [
    ("client_id", "library.book", "library_book", "many2one", False, "library"),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.add_fields(env, _field_adds)
    openupgrade.logged_query(
        env.cr,
        """
            UPDATE library_book
            SET client_id = partner_id
        """,
    )
