from .base_csv_loader import BaseCsvLoader


class ProductCategoryLoader(BaseCsvLoader):
    model_name = "product.category"
    folder = "product_category"
    filters = {}