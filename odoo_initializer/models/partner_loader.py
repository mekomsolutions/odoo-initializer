from .base_csv_loader import BaseCsvLoader


class PartnerLoader(BaseCsvLoader):
    model_name = "res.partner"
    folder = "partner"
    filters = {}