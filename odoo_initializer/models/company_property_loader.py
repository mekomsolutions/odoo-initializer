from .base_csv_loader import BaseCsvLoader


class CompanyPropertyLoader(BaseCsvLoader):
    update_existing_record = True
    model_name = "ir.property"
    folder = "company_property"
    filters = {}
