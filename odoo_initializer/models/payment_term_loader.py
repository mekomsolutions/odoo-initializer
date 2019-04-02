from .base_loader import BaseModelLoader


class PaymentTermLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.payment.term"
    folder = "payment_term"
    filters = {}
