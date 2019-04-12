from odoo.tests import logging
from odoo import tests

from ..utils import config
from ..utils.data_files_utils import data_files

_logger = logging.getLogger(__name__)


class TestDataFilesUtils(tests.BaseCase):
    @staticmethod
    def _get_test_file():
        file_ = open("/etc/odoo/odoo.conf", "r")
        return file_.name

    def test_get_default_checksum_path(self):
        # Setup
        config.checksum_folder = None

        # Replay
        checksum_path = data_files.get_checksum_path(self._get_test_file())

        # Verify
        assert checksum_path == "/etc_checksum/odoo/odoo.conf.checksum"

    def test_get_custom_checksum_path(self):

        # Setup
        config.checksum_folder = "/custom/data_checksum"

        # Replay
        checksum_path = data_files.get_checksum_path(self._get_test_file())

        # Verify
        assert checksum_path == "/custom/data_checksum/odoo/odoo.conf.checksum"
