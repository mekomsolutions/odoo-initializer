from .base_loader import BaseLoader


class DrugLoader(BaseLoader):
    model_name = "product.template"
    field_mapping = {
        "product_variant_ids/id": "odoo_id",
        "id": "odoo_id",
    }
    folder = "drugs"
    filters = {}
