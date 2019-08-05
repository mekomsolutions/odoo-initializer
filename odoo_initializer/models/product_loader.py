from .base_csv_loader import BaseCsvLoader


class ProductLoader(BaseCsvLoader):
    model_name = "product.template"
    folder = "product"
    filters = {}
