from .base_loader import BaseLoader


class ProductLoader(BaseLoader):
    model_name = "product.template"
    folder = "product"
    filters = {}
    field_rules = {
        "lst_price": "NO_UPDATE"
    }
