from .base_csv_loader import BaseCsvLoader


class JournalLoader(BaseCsvLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.journal"
    folder = "journals"
    filters = {}
