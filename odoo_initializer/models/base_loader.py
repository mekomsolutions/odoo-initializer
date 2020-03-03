import logging

import odoo
from odoo import api
from odoo.api import Environment

from ..utils.config import config
from ..utils.data_files_utils import data_files

_logger = logging.getLogger(__name__)


class BaseLoader:
    def __init__(self):
        pass

    model_name = None
    fields = None
    test = False
    allowed_file_extensions = [".csv"]
    field_mapping = None
    folder = None
    filters = {}

    def load_files(self, relevant_folder):
        return data_files.get_files(
            relevant_folder, allowed_extensions=self.allowed_file_extensions
        )

    def load_file(self, file_):
        if not file_:
            return []
        with api.Environment.manage():
            registry = odoo.registry(config.db_name)
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                # fetching the list of models available in database
                cr.execute('SELECT model FROM ir_model ')
                models = cr.dictfetchall()

                # Checking if the model is available in database
                found = False
                for model in models:
                    if model['model'] == self.model_name:
                        found = True

                if not found:
                    _logger.warn("model " + self.model_name + " not found.")
                    return False

                # If model is available in database but not in the environment, Delete registry to provoke refreshing
                # the list of models

                if found and (self.model_name not in odoo.api.Environment(cr, uid, {})):
                    registry.delete(config.db_name)

                ctx = odoo.api.Environment(cr, uid, {})['res.users'].context_get()
                env = odoo.api.Environment(cr, uid, ctx)

                model = env["base_import.import"]
                import_wizard = model.create(
                    {
                        "res_model": self.model_name,
                        "file": file_,
                        "file_type": "text/csv",
                    }
                )
                result = import_wizard.do(
                    self.fields, {"quoting": '"', "separator": ",", "headers": True}
                )
        return True

    def _validate_mapping(self, mapping, file_header):
        validated_mapping = {}
        if not mapping:
            for key in file_header:
                validated_mapping[key] = key
        else:
            for field in mapping.items():
                if field[1] in file_header:
                    validated_mapping[field[0]] = field[1]
                else:
                    validated_mapping = {}
                    _logger.warn("Skipping file import, Field '" + field[1] + "' is missing")
                    break
        return validated_mapping

    def _mapper(self, file_, mapping, filters_):
        if not isinstance(filters_, dict):
            filters_ = {}
        mapped_dict = []
        if not file_:
            return []
        if (not isinstance(file_, dict)) and (not isinstance(file_, list)):
            return file_
        file_header = file_[0].keys()

        mapping = self._validate_mapping(mapping, file_header)
        self.fields = mapping.keys()

        for dict_line in file_:
            to_map = False

            if not filters_:
                to_map = True

            for filter_key, filter_value in filters_.items():
                if filter_key in dict_line.keys():
                    filter_value = (
                        [filter_value]
                        if not isinstance(filter_value, list)
                        else filter_value
                    )
                    if dict_line[filter_key] in filter_value:
                        to_map = True

            # If the Line is not filtered out then we apply the mapping and add it
            if to_map:
                mapped_row = {}
                for key, value in mapping.items():
                    if value in dict_line.keys():
                        mapped_row[key] = dict_line.pop(value)
                mapped_dict.append(mapped_row)

        return data_files.build_csv(mapped_dict) if mapped_dict else []
                
    def load_(self):
        _logger.info("file loading")
        for file_ in self.load_files(self.folder):
            file_content = data_files.get_file_content(file_, self.allowed_file_extensions)
            mapped_file = self._mapper(file_content, self.field_mapping, self.filters)
            if self.load_file(mapped_file):
                data_files.create_checksum_file(data_files.get_checksum_path(file_), data_files.md5(file_))
