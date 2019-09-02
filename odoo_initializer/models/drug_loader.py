from .base_csv_loader import BaseCsvLoader


class DrugLoader(BaseCsvLoader):
    model_name = "product.template"
    field_mapping = {
        "lst_price": "odoo_price",
        "product_variant_ids/categ_id/id": "odoo_category",
        "type":"odoo_type",
        "name": "Name",
        "product_variant_ids/uuid": "Uuid",
        "id": "odoo_id",
    }
    folder = "drugs"
    filters = {}
