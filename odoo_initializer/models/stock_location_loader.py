from .base_csv_loader import BaseCsvLoader


class StockLocationLoader(BaseCsvLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "stock.location"
    folder = "stock_location"
    filters = {}
