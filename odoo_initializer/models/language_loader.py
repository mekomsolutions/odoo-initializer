import odoo
from odoo import api
from ..utils.config import config

from .base_loader import BaseLoader


class LanguageLoader(BaseLoader):
    folder = "language"
    model_name = "res.lang"
    allowed_file_extensions = ".xml"
    filters = {}

    def load_file(self, file_):
        if not file_:
            return []
        with api.Environment.manage():
            registry = odoo.registry(config.db_name)
            with registry.cursor() as cr:

                uid = odoo.SUPERUSER_ID
                ctx = odoo.api.Environment(cr, uid, {})['res.users'].context_get()
                env = odoo.api.Environment(cr, uid, ctx)
                model = env[self.model_name]

                for lang in file_:
                    model.load_lang(lang.text)
        return
