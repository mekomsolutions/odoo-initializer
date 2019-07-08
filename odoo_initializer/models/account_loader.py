from .base_csv_loader import BaseCsvLoader


class AccountLoader(BaseCsvLoader):
    model_name = "account.account"
    folder = "account"
    filters = {}
