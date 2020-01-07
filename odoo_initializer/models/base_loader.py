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
            registry = odoo.modules.registry.RegistryManager.get(config.db_name)
            if not self.test:
                registry.delete_all()
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
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
                _logger.info("import done")
        return result

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

    def _model_exist(self):
        with api.Environment.manage():
            registry = odoo.modules.registry.RegistryManager.get(config.db_name)
            if not self.test:
                registry.delete_all()
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
                return self.model_name in env
                
    def load_(self):
        _logger.info("file loading")
        for file_ in self.load_files(self.folder):
            if self._model_exist():
                mapped_file = self._mapper(file_, self.field_mapping, self.filters)
                self.load_file(mapped_file)
            else:
                _logger.warn('the model"' + self.model_name + '" does not exist')
