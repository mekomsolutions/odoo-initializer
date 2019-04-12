import logging

from .base_csv_loader import BaseCsvLoader

_logger = logging.getLogger(__name__)


class PriceListLoader(BaseCsvLoader):
    model_name = "product.pricelist"
    folder = "pricelist"

