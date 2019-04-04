from .base_csv_loader import BaseCsvLoader


class FiscalPositionLoader(BaseCsvLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.fiscal.position"
    folder = "fiscal_position"
    filters = {}
