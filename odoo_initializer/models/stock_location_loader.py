from .base_loader import BaseModelLoader


class StockLocationLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "stock.location"
    folder = "stock_location"
    filters = {}