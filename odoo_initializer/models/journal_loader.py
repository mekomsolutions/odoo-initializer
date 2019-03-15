from .base_loader import BaseModelLoader


class JournalLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.journal"
    folder = "journals"
    filters = {}
