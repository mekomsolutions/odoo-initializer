from .base_csv_loader import BaseCsvLoader


class SaleShopLoader(BaseCsvLoader):
    model_name = "sale.shop"
    folder = "sale_shop"
    filters = {}
