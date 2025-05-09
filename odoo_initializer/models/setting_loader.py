import logging


from .base_loader import BaseLoader
from ..utils.registry import registry
from odoo.tools.convert import xml_import
import xml.etree.ElementTree as ET

_logger = logging.getLogger(__name__)


class SettingLoader(BaseLoader):
    model_name = "base.setting"
    folder = "setting"
    allowed_file_extensions = ".xml"

    def load_file(self, file_: ET.Element):
        xml = xml_import(registry.env, "odoo_initializer", {}, "init", False, "")
        xml.parse(file_)
        return True
