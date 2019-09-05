from .base_csv_loader import BaseCsvLoader


class CurrencyLoader(BaseCsvLoader):
    model_name = "res.currency"
    folder = "currency"
    filters = {}