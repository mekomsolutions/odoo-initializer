import logging

import odoo
from odoo import api
from odoo.api import Environment

from ..utils.config import config
from ..utils.data_files_utils import data_files

_logger = logging.getLogger(__name__)


class BaseCsvLoader:
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
            relevant_folder,
            allowed_extensions=self.allowed_file_extensions,
        )

    def load_file(self, file_):

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
        return result

    def _validate_mapping(self, mapping, file_header):
        validated_mapping = {}
        with api.Environment.manage():
            registry = odoo.modules.registry.RegistryManager.get(config.db_name)
            if not self.test:
                registry.delete_all()
            with registry.cursor() as cr:
                uid = odoo.SUPERUSER_ID
                env = Environment(cr, uid, {})
                model = env[self.model_name]
                model_fields = model.fields_get()
        if not mapping:
            for key in file_header:
                validated_mapping[key] = key
        else:
            for field in mapping.items():
                for model_field in model_fields.items():
                    if field[0] == model_field[0]:
                        validated_mapping[field[0]] = field[1]
                        break

        return validated_mapping

    def _mapper(self, file_, mapping, filters_):
        if not isinstance(filters_, dict):
            filters_ = {}
        mapped_dict = []
        file_header = file_[0].keys()

        mapping = self._validate_mapping(mapping, file_header)
        self.fields = mapping.keys()
        for dict_line in file_:
            row = {}
            for key, value in mapping.items():
                if value in dict_line.keys():
                    row[key] = dict_line.pop(value)

            if not filters_:
                mapped_dict.append(row)

            for filter_key, filter_value in filters_.items():
                if filter_key in row.keys():
                    filter_value = (
                        [filter_value]
                        if not isinstance(filter_value, list)
                        else filter_value
                    )
                    if row[filter_key] in filter_value:
                        mapped_dict.append(row)

        mapped_csv = data_files.build_csv(mapped_dict)
        return mapped_csv

    def load_(self):
        _logger.info("file loading")
        for file_ in self.load_files(self.folder):
            mapped_file = self._mapper(file_, self.field_mapping, self.filters)

            self.load_file(mapped_file)
