import os
import tempfile
from os.path import basename

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
        model_name = "res.partner"

        # Replay
        checksum_path = data_files.get_checksum_path(self._get_test_file(), model_name)

        # Verify
        _logger.info("LAKSJDLASJDLKANSFLJANFLJANSLD_LLS_KA")
        _logger.info(checksum_path)
        assert checksum_path == "/etc_checksum/odoo/res.partner_odoo.conf.checksum"

    def test_get_custom_checksum_path(self):
        # Setup
        config.checksum_folder = "/custom/data_checksum"
        model_name = "res.partner"

        # Replay
        checksum_path = data_files.get_checksum_path(self._get_test_file(), model_name)

        # Verify
        _logger.info("LAKSJDLASJDLKANSFLJANFLJANSLDKA")
        _logger.info(checksum_path)
        assert checksum_path == "/custom/data_checksum/odoo/res.partner_odoo.conf.checksum"

    def test_get_files_should_get_files_by_extension(self):
        # Create config directories

        model_name = "res.partner"
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
        files = data_files.get_files(basename(data_dir), ".csv", model_name)
        # Verify
        assert len(files) == 3

    def test_create_checksum_when_file_loaded(self):
        # Create config directories
        model_name = "res.partner"
        temp_dir = tempfile.mkdtemp()
        config_checksum_dir = tempfile.mkdtemp(dir=temp_dir)
        config.checksum_folder = config_checksum_dir

        file__ = data_files.get_checksum_path(self._get_test_file(), model_name)
        checksum = data_files.md5(self._get_test_file())

        # Replay
        file_processed = data_files.file_already_processed(self._get_test_file(), model_name)
        data_files.create_checksum_file(file__, checksum)

        # Verify
        assert not file_processed
        assert os.path.exists(os.path.join(config_checksum_dir, "odoo/res.partner_odoo.conf.checksum"))
