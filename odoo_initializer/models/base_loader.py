import logging

import odoo
from odoo import api
from odoo.api import Environment

from ..utils.config_loader import config_loader

_logger = logging.getLogger(__name__)


class BaseModelImporter:
    def __init__(self):
        pass

    model_name = None
    _model = None
    data_files_source = "odoo"  # ["openmrs, "odoo"]
    update_existing_record = False
    identifier = None
    allowed_file_extensions = [
        ".csv"
    ]  # supported file extensions [".csv", ".xls", ".xlsx"]
    field_mapping = None
    folder = None
    filters = {}

    def load_files(self, relevant_folder):
        return config_loader.get_files(
            self.data_files_source,
            relevant_folder,
            allowed_extensions=self.allowed_file_extensions,
        )

    def load_file(self, file_):

        with api.Environment.manage():
            registry = odoo.modules.registry.RegistryManager.get(config_loader._db_name)
            with registry.cursor() as cr:
                registry.delete_all()
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
                model = env[self.model_name]

                for record in file_:
                    found_records = model.search(
                        [(self.identifier, "=", record[self.identifier])]
                    )
                    # TODO: what if there are multiple records found for the same record.
                    #  for now taking only the first record into consideration
                    if found_records and not self.update_existing_record:
                        _logger.info("Existing record with ID:" + str(found_records[0]) + "skipped.")
                        continue

                    if found_records:
                        found_records[0].write(record)
                        _logger.info(
                            "Existing record with ID:" + str(found_records[0]) + "updated."
                        )
                    else:
                        saved_record = model.create(record)
                        _logger.info("New record with ID:" + str(saved_record) + "created.")

        return file_

    def _validate_mapping(self, mapping):
        validated_mapping = {}
        with api.Environment.manage():
            registry = odoo.modules.registry.RegistryManager.get(config_loader._db_name)
            with registry.cursor() as cr:
                registry.delete_all()
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
                model = env[self.model_name]
                model_keys = model.fields_get()
        if not mapping:
            for key in model_keys.items():
                validated_mapping[key[1].string] = key[1].string
        # TODO: check the match between keys and mappings
        return validated_mapping or mapping

    def _mapper(self, file_, mapping, filters_):
        if not isinstance(filters_, dict):
            filters_ = {}
        mapped_csv = []

        mapping = self._validate_mapping(mapping)
        for dict_line in file_:
            row = {}
            for key, value in mapping.items():
                if value in dict_line.keys():
                    row[key] = dict_line.pop(value)

            if not filters_:
                mapped_csv.append(row)

            for filter_key, filter_value in filters_.items():
                if filter_key in row.keys():
                    filter_value = (
                        [filter_value]
                        if not isinstance(filter_value, list)
                        else filter_value
                    )
                    if row[filter_key] in filter_value:
                        mapped_csv.append(row)
        return mapped_csv

    def load_(self):
        _logger.info("file loading")
        for file_ in self.load_files(self.folder):
            mapped_file = self._mapper(file_, self.field_mapping, self.filters)

            self.load_file(mapped_file)
