from odoo.tests import logging
from odoo import tests

from ..models import BaseLoader

_logger = logging.getLogger(__name__)


class TestLoader(tests.TransactionCase):

    _test_model = "res.groups"

    @staticmethod
    def _get_groups():
        return [
            {"id": "group_test_1", "name": "test_1", "comment": "other"},
            {"id": "group_test_2", "name": "test_2", "comment": "filter"},
            {"id": "group_test_3", "name": "test_3", "comment": "other"},  # , "invoice_warn": "No Message"
        ]

    @staticmethod
    def _get_partners():
        return [
            {"id": "partner_1",
             "name": "partner 1",
             "local_name": "refer to group:${group_test_1}"
             }
        ]

    def test_filter_applied(self):

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        test_loader.filters = {"comment": "filter"}

        # Replay
        filtered_groups = test_loader._mapper(
            self._get_groups(), None, test_loader.filters
        )

        # Verify
        assert "other" not in filtered_groups

    def test_no_update_rule_should_not_update_comment(self):

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        test_loader.field_rules = {
            "comment": "NO_UPDATE"
        }
        test_loader.fields = ["id", "name", "comment"]

        # Replay
        test_loader.load_file(test_loader._mapper(
            self._get_groups(), None, None)
        )
        filtered_groups = test_loader._mapper(
            self._get_groups(), None, None
        )

        # Verify
        assert "comment" not in filtered_groups

    def test_external_to_internal_id_rule_should_replace_group_id(self):

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        test_loader.fields = ["id", "name", "comment"]
        test_loader.load_file(test_loader._mapper(
            self._get_groups(), None, None)
        )
        test_loader.field_rules = {
            "local_name": "EXTERNAL_TO_INTERNAL_ID"
        }

        # Replay
        filtered_partners = test_loader._mapper(
            self._get_partners(), None, None
        )

        # Verify
        assert filtered_partners.split("refer to group:", 1)[1].split(",")[0].rstrip().isdigit()
