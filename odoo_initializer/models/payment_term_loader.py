from .base_csv_loader import BaseCsvLoader


class PaymentTermLoader(BaseCsvLoader):
    model_name = "account.payment.term"
    folder = "payment_term"
    filters = {}
