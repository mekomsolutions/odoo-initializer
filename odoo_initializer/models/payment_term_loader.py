from .base_csv_loader import BaseCsvLoader


class PaymentTermLoader(BaseCsvLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.payment.term"
    folder = "payment_term"
    filters = {}
