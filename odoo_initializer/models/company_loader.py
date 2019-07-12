from .base_csv_loader import BaseCsvLoader


class CompanyLoader(BaseCsvLoader):
    model_name = "res.company"
    folder = "company"
    filters = {}
