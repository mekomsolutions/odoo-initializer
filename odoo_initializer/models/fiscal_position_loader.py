from .base_loader import BaseModelLoader


class FiscalPositionLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.fiscal.position"
    folder = "fiscal_postion"
    filters = {}
