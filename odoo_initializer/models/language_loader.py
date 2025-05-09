import logging

from ..utils.registry import registry

from .base_loader import BaseLoader

_logger = logging.getLogger(__name__)


class LanguageLoader(BaseLoader):
    folder = "language"
    model_name = "base.language.install"
    allowed_file_extensions = ".xml"
    filters = {}

    def load_file(self, file_):
        if not file_:
            return []
        env = registry.env
        model = env[self.model_name]
        for lang in file_:
            language = env['res.lang'].search([("code", "=", lang.text), ("active", "=", False)])
            if language.id:
                model.create({'lang_ids': [language.id]}).lang_install()
        return True
