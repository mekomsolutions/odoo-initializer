import odoo
from odoo import api
from odoo.api import Environment
from ..utils.config import config

from .base_loader import BaseLoader


class LanguageLoader(BaseLoader):
    folder = "language"
    model_name = "base.language.install"
    allowed_file_extensions = ".xml"
    filters = {}

    def load_file(self, file_):
        if not file_:
            return []
        with api.Environment.manage():
            registry = odoo.registry(config.db_name)
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
                model = env[self.model_name]
                for lang in file_:
                    installer = model.create({'lang': lang.text})
                    installer.lang_install()
        return
