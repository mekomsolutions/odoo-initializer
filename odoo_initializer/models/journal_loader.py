from .base_csv_loader import BaseCsvLoader


class JournalLoader(BaseCsvLoader):
    model_name = "account.journal"
    folder = "journal"
    filters = {}
