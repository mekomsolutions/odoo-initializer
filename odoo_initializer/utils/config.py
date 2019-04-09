import logging
import odoo.tools.config

_logger = logging.getLogger(__name__)


class Config:
    def __init__(self):
        try:
            self.openmrs_path = odoo.tools.config["openmrs_initializer_path"]
        except KeyError:
            self.openmrs_path = None
            _logger.warn("'openmrs_initializer_path' variable is not set")
        try:
            self.odoo_path = odoo.tools.config["odoo_initializer_path"]
        except KeyError:
            _logger.warn(
                "'odoo_initializer_path' is not set, using 'data_dir' path as default"
            )
            self.odoo_path = odoo.tools.config["data_dir"]
        try:
            self.db_name = odoo.tools.config["db_name"]
        except KeyError:
            pass
        try:
            self.checksum_folder = odoo.tools.config["initializer_checksums"]
        except KeyError:
            self.checksum_folder = None


config = Config()
