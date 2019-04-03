from .base_loader import BaseModelLoader


class CompanyPropertyLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "ir.property"
    folder = "company_property"
    filters = {}
