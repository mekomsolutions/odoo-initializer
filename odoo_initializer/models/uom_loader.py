import logging

from .base_loader import BaseLoader

_logger = logging.getLogger(__name__)


class UOMLoader(BaseLoader):
    model_name = "product.uom"
    folder = "units_of_measure"
