import logging

from .base_loader import BaseModelLoader

_logger = logging.getLogger(__name__)


class JournalLoader(BaseModelLoader):
    update_existing_record = True
    data_files_source = "odoo"
    model_name = "account.journal"
    folder = "journals"
    filters = {}
    identifier = "name"
