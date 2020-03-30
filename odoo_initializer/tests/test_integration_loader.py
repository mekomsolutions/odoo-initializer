from odoo import tests
from odoo.tests import logging

from ..models import BaseLoader

_logger = logging.getLogger(__name__)


class TestLoader(tests.TransactionCase):
    _test_model = "res.groups"

    @staticmethod
    def _get_non_updated_groups():
        return [
            {"id": "group_test_1", "name": "test_1", "comment": "other"},
            {"id": "group_test_2", "name": "test_2", "comment": "filter"},
            {"id": "group_test_3", "name": "test_3", "comment": "other"},
        ]

    @staticmethod
    def _get_updated_groups():
        return [
            {"id": "group_test_1", "name": "test_1", "comment": "other"},
            {"id": "group_test_3", "name": "test_3", "comment": "updated comment"},
        ]

    def test_no_update_rule_should_not_update_comment(self):  # Add updated groups records and test it with load_file()

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        test_loader.field_rules = {
            "comment": "NO_UPDATE"
        }
        test_loader.fields = ["id", "name", "comment"]
        test_loader.load_file(
            test_loader._pre_process(self._get_non_updated_groups(), None, None)
        )

        # Replay
        processed_file = test_loader._pre_process(self._get_updated_groups(), None, None)

        test_loader.load_file(
            processed_file
        )

        # Verify
        assert "updated comment" not in processed_file

    def test_external_to_internal_id_rule_should_replace_group_id(self):  # Test record existing

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        test_loader.fields = ["id", "name", "comment"]
        test_loader.load_file(test_loader._pre_process(
            self._get_non_updated_groups(), None, None)
        )
        test_loader.field_rules = {
            "comment": "EXTERNAL_TO_INTERNAL_ID"
        }

        # Replay
        processed_file = test_loader._pre_process(
            [
                {"id": "new_group",
                 "name": "New Group",
                 "comment": "refer to group:${group_test_1}"
                 }
            ], None, None
        )

        test_loader.load_file(
            processed_file
        )

        # Verify
        reference_value = processed_file.split("refer to group:", 1)[1].split(",")[0].rstrip()
        assert reference_value.isdigit()
        assert int(reference_value) == test_loader._record_exist("group_test_1")[0].get('res_id')
