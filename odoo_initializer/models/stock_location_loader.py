from .base_csv_loader import BaseCsvLoader


class StockLocationLoader(BaseCsvLoader):
    model_name = "stock.location"
    folder = "stock_location"
    filters = {}
