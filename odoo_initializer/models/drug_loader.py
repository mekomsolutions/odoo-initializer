from .base_csv_loader import BaseCsvLoader


class DrugLoader(BaseCsvLoader):
    model_name = "product.template"
    field_mapping = {
        "id": "Uuid",
        "name": "Name",
        "drug": "Concept Drug",
        "lst_price": "odoo_price",
        "categ_id/id": "odoo_category",
    }
    folder = "drugs"
    filters = {}
