from .base_csv_loader import BaseCsvLoader


class CompanyPropertyLoader(BaseCsvLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "ir.property"
    folder = "company_property"
    filters = {}
