from .base_loader import BaseLoader


class DrugLoader(BaseLoader):
    model_name = "product.template"
    field_mapping = {
        "lst_price": "odoo_price",
        "product_variant_ids/categ_id/id": "odoo_category",
        "type":"odoo_type",
        "name": "Name",
        "product_variant_ids/uuid": "Uuid",
        "id": "odoo_id",
        "uom_id/id": "odoo_uom",
        "standard_price": "odoo_cost"
    }
    folder = "drugs"
    filters = {}
