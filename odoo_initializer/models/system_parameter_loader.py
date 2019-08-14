from .base_csv_loader import BaseCsvLoader


class SystemParameterLoader(BaseCsvLoader):
    model_name = "ir.config_parameter"
    folder = "system_parameter"
    filters = {}