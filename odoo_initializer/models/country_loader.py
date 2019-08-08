from .base_csv_loader import BaseCsvLoader


class CountryLoader(BaseCsvLoader):
    model_name = "res.country"
    folder = "country"
    filters = {}
