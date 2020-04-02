from odoo.tests import logging
from odoo import tests

from ..models import BaseLoader

_logger = logging.getLogger(__name__)


class TestLoader(tests.BaseCase):
    _test_model = "res.groups"

    @staticmethod
    def _get_groups():
        return [
            {"id": "group_test_1", "name": "test_1", "comment": "other"},
            {"id": "group_test_2", "name": "test_2", "comment": "filter"},
            {"id": "group_test_3", "name": "test_3", "comment": "other"},
        ]

    def test_validate_mapping_should_return_empty_if_not_valid(self):

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        field_mapping = {
            "lst_price": "not_odoo_price",
            "product_variant_ids/categ_id/id": "odoo_category",
            "type": "odoo_type",
        }
        file_header = ["odoo_price", "odoo_category", "odoo_type"]

        # Replay
        validated_mapping = test_loader._validate_mapping(field_mapping, file_header)

        # Verify
        assert validated_mapping == {}

    def test_validate_mapping_should_return_same_if_valid(self):

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        field_mapping = {
            "lst_price": "odoo_price",
            "product_variant_ids/categ_id/id": "odoo_category",
            "type": "odoo_type",
        }
        file_header = ["odoo_price", "odoo_category", "odoo_type"]

        # Replay
        validated_mapping = test_loader._validate_mapping(field_mapping, file_header)

        # Verify
        assert validated_mapping == {
            "lst_price": "odoo_price",
            "product_variant_ids/categ_id/id": "odoo_category",
            "type": "odoo_type",
        }

    def test_filter_applied(self):

        # Setup
        test_loader = BaseLoader()
        test_loader.model_name = self._test_model
        test_loader.filters = {"comment": "filter"}

        # Replay
        filtered_groups = test_loader._pre_process(
            self._get_groups(), None, test_loader.filters
        )

        # Verify
        assert "other" not in filtered_groups
