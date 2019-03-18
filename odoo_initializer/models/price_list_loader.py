import logging

from .base_loader import BaseModelLoader

_logger = logging.getLogger(__name__)


class PriceListLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "openmrs"
    model_name = "product.pricelist"
    folder = "pricelist"

