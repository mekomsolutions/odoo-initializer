from .base_csv_loader import BaseCsvLoader


class OrderTypeLoader(BaseCsvLoader):
    model_name = "order.type"
    folder = "order_type"
    filters = {}
