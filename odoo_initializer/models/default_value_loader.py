from .base_csv_loader import BaseCsvLoader


class DefaultValueLoader(BaseCsvLoader):
    model_name = "ir.values"
    folder = "default_value"
    filters = {}