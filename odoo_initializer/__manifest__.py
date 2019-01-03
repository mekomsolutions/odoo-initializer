{
    "name": "initz",
    "summary": """
        Odoo metadata/data initializer""",
    "description": """
        an odoo module to import data and metadata provided by openmrs config
    """,
    "author": "MekomSolutions",
    "website": "http://www.mekomsolutions.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "base_import"],
    "external_dependencies": {"python" : ["odoorpc"]},
    "application": True,
    "installable": True,
    "auto_install": True
}

