import logging

from .models.price_list_loader import PriceListLoader
from .models.journal_loader import JournalLoader
from .models.fiscal_position_loader import FiscalPositionLoader
from .models.drug_loader import DrugLoader

_logger = logging.getLogger(__name__)

_logger.info("start initialization process")

registered_loader = [FiscalPositionLoader, JournalLoader, DrugLoader, PriceListLoader]

for loader_class in registered_loader:
    loader = loader_class()
    loader.load_()


_logger.info("initialization done")
