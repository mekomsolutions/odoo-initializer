import logging

from .base_loader import BaseModelLoader

_logger = logging.getLogger(__name__)


class DrugLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "openmrs"
    model_name = "product.template"
    field_mapping = {"name": "name", "drug_name": "Fully specified name:en", "lst_price": "odoo_price"}
    folder = "drugs"
    filters = {}
    identifier = "name"
