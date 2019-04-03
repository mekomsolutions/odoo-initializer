from .base_loader import BaseModelLoader


class DrugLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "openmrs"
    model_name = "product.template"
    field_mapping = {
        "id": "id",
        "name": "name",
        "drug": "Fully specified name:en",
        "lst_price": "odoo_price",
    }
    folder = "drugs"
    filters = {}
