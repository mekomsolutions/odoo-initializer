from .base_csv_loader import BaseCsvLoader


class FiscalPositionLoader(BaseCsvLoader):
    model_name = "account.fiscal.position"
    folder = "fiscal_position"
    filters = {}
