import odoo
from odoo import api
from odoo.api import Environment
from ..utils.config import config

from .base_loader import BaseLoader, _logger


class LanguageLoader(BaseLoader):
    folder = "language"
    model_name = "res.lang"
    allowed_file_extensions = ".xml"
    filters = {}

    def load_file(self, file_):

        if not file_:
            return []
        with api.Environment.manage():
            registry = odoo.modules.registry.RegistryManager.get(config.db_name)
            if not self.test:
                registry.delete_all()
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
                model = env[self.model_name]
                for lang in file_:
                    model.load_lang(lang.text)
        return
