import os
import tempfile
from os.path import dirname, basename

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

    def test_get_files(self):
        # Create config directories

        temp_dir = tempfile.mkdtemp()
        config_dir = tempfile.mkdtemp(dir=temp_dir)
        data_dir = tempfile.mkdtemp(dir=config_dir)
        config.data_files_paths = [config_dir]
        config.checksum_folder = None

        # create example data files
        open(os.path.join(data_dir, "file_1.csv"), "a")
        open(os.path.join(data_dir, "file_2.csv"), "a")
        open(os.path.join(data_dir, "file_3.csv"), "a")
        open(os.path.join(data_dir, "file_4.xml"), "a")

        # Replay
        files = data_files.get_files(basename(data_dir), ".csv")
        files_already_processed = data_files.get_files(basename(data_dir), ".csv")

        # Verify
        assert len(files) == 3
        assert len(files_already_processed) == 0
