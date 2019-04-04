import logging

from .base_csv_loader import BaseCsvLoader

_logger = logging.getLogger(__name__)


class PriceListLoader(BaseCsvLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "product.pricelist"
    folder = "pricelist"

