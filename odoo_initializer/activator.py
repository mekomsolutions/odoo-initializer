import logging

from models.drug_loader import DrugLoader


_logger = logging.getLogger(__name__)

registered_loader = [DrugLoader]


for loader_class in registered_loader:
    loader = loader_class()
    loader.load_()

_logger.info("done")
