import logging
from os.path import basename

import odoo
from odoo import api

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
    field_rules = {}

    def apply_rules(self, record={}, rules={}):

        # all rules should be registered here
        _rules_register = {
            "NO_UPDATE": self._no_update_rule,
            "EXTERNAL_TO_INTERNAL_ID": self._external_to_internal_id_rule,
        }

        for rule_field, rule_name in rules.items():
            record = _rules_register.get(rule_name)(record, rule_field)

        return record

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
                cr.execute('SELECT model FROM ir_model ')
                models = cr.dictfetchall()

                # Checking if the model is available in database
                found = False
                for model in models:
                    if model['model'] == self.model_name:
                        found = True

                if (not config.init) and found and (self.model_name not in odoo.api.Environment(cr, uid, {})):
                    _logger.info("Updating registry once")
                    registry.delete(config.db_name)
                    config.init = True

                if self.model_name not in odoo.api.Environment(cr, uid, {}):
                    _logger.warn("Model '" + self.model_name + "' not found.")
                    return False

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

    def _pre_process(self, file_, mapping, filters_):
        if not isinstance(filters_, dict):
            filters_ = {}
        mapped_dict = []
        if not file_:
            return []
        if (not isinstance(file_, dict)) and (not isinstance(file_, list)):
            return file_
        file_header = file_[0].keys()
        mapping = self._validate_mapping(mapping, file_header)
        if not mapping:
            return []
        for dict_line in file_:
            to_map = False

            if (not filters_) and (not self.field_rules):
                to_map = True

            # Apply rule and mark it to be mapped if any is set
            if self.field_rules:
                record = self.apply_rules(dict_line, self.field_rules)
                dict_line = record
                to_map = True

            # Do not map row if filters applies
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

        self.fields = mapped_dict[0].keys()
        return data_files.build_csv(mapped_dict) if mapped_dict else []

    def _record_exist(self, record_id):
        with api.Environment.manage():
            registry = odoo.registry(config.db_name)
            with registry.cursor() as cr:
                cr.execute("SELECT res_id FROM ir_model_data WHERE name='" + record_id + "';")
                return cr.dictfetchall() or False

    # Rule to delete a field that shouldn't be updated if found, from the record
    def _no_update_rule(self, record=None, field=None):
        if record is None:
            record = {}
        updated_record = dict(record)
        if not self._record_exist(record.get("id")):
            return record
        if field in record:
            updated_record.pop(field)
            return updated_record
        return record

    # Rule to replace a record referenced by external id with its internal id
    def _external_to_internal_id_rule(self, record=None, field=None):
        if record is None:
            record = {}
        updated_record = dict(record)
        field_origin_value = record.get(field)
        external_id = data_files.extract_reference(field_origin_value)
        if not external_id:
            return updated_record
        result = self._record_exist(external_id)
        if result:
            field_value = data_files.replace_reference(field_origin_value, str(result[0].get('res_id')))
            updated_record[field] = field_value
        return updated_record

    def load_(self):
        _logger.info("Loading files for model: " + self.model_name)
        for file_ in self.load_files(self.folder):
            file_content = data_files.get_file_content(file_, self.allowed_file_extensions)
            mapped_file = self._pre_process(file_content, self.field_mapping, self.filters)
            if self.load_file(mapped_file):
                _logger.info("File loaded successfully: " + basename(file_))
                data_files.create_checksum_file(data_files.get_checksum_path(file_), data_files.md5(file_))
            else:
                _logger.warn("File cannot be loaded: " + basename(file_))
