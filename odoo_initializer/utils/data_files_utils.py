import logging
import os
import hashlib
import csv
from .config import config

_logger = logging.getLogger(__name__)

from os.path import dirname, basename, split


class DataFilesUtils:

    @staticmethod
    def get_data_folder_path(data_files_source):
        data_files_source = data_files_source.lower()
        assert data_files_source in ["odoo", "openmrs"]
        return (
            config.openmrs_path if data_files_source == "openmrs" else config.odoo_path
        )

    def get_files(self, data_files_source, folder, allowed_extensions):
        import_files = []
        if not self.get_data_folder_path(data_files_source):
            _logger.warn(ValueError("Invalid config path"))
            return []
        path = os.path.join(self.get_data_folder_path(data_files_source), folder)
        _logger.info("path:" + path)
        for root, dirs, files in os.walk(path):
            for file_ in files:
                file_path = os.path.join(path, file_)

                filename, ext = os.path.splitext(file_)
                if str(ext).lower() in allowed_extensions:
                    if self.file_already_processed(file_path):
                        _logger.info("Skipping already processed file: " + str(file_))
                        continue
                    with open(os.path.join(path, file_), "r") as file_data:
                        extracted_csv = csv.DictReader(file_data)
                        csv_dict = []
                        for row in extracted_csv:
                            csv_dict.append(row)
                        import_files.append(csv_dict)
        return import_files

    def file_already_processed(self, file_):
        file_name = basename(file_)
        file_dir = split(dirname(file_))[1]
        checksum_dir = split(dirname(file_))[0] + "_checksum"
        checksum_path = os.path.join(checksum_dir, file_dir, file_name) + ".checksum"
        md5 = self.md5(file_)
        if os.path.exists(checksum_path):
            with open(checksum_path, "r") as f:
                old_md5 = f.read()
                if old_md5 != md5:
                    f.close()
                    with open(checksum_path, "w") as fw:
                        fw.write(md5)
            return old_md5 == md5
        if not os.path.isdir(dirname(checksum_path)):
            try:
                os.makedirs(dirname(checksum_path))
            except OSError:
                raise
        with open(checksum_path, "w") as f:
            f.write(md5)
        return False

    @staticmethod
    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


data_files = DataFilesUtils()
