import logging

from .base_loader import BaseModelImporter

_logger = logging.getLogger(__name__)


class DrugLoader(BaseModelImporter):
    update_existing_record = True
    data_files_source = "openmrs"
    model_name = "product.template"
    field_mapping = {"name": "Fully specified name:en", "lst_price": "odoo_price"}
    folder = "concepts"
    filters = {}
    identifier = "name"
