from odoo.tests import logging
from odoo import tests

from ..models import BaseModelLoader

_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(tests.TransactionCase):

    _test_model = "res.partner"

    @staticmethod
    def _get_duplicate_partners():
        return [
            {"name": "partner_1"},
            {"name": "partner_2"},
            {"name": "partner_1"},
            {"name": "partner_3"},
        ]

    @staticmethod
    def _get_unfiltered_partners():
        return [
            {"name": "test_1", "website": "example.com"},
            {"name": "test_2", "website": "example.com"},
            {"name": "test_3", "website": "test.com"},
            {"name": "test_4", "website": "example.com"},
            {"name": "test_4", "website": "site.com"},
        ]

    def test_no_duplicates(self):

        # Setup
        test_loader = BaseModelLoader()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"

        # Replay
        test_loader.load_file(self._get_duplicate_partners())

        # Verify
        model = self.env[self._test_model]
        result = model.search([(test_loader.identifier, "=", "partner_1")])

        # Assert that only one record is created per identifier
        assert len(result) == 1, "a duplicate record was found."

    def test_update_record(self):

        # Setup
        partner_name = "partner_x"
        old_phone = "0167771"
        updated_phone = "010110"

        test_loader = BaseModelLoader()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"
        test_loader.update_existing_record = True

        test_loader.load_file([{"name": partner_name, "phone": old_phone}])

        # Replay
        test_loader.load_file([{"name": partner_name, "phone": updated_phone}])

        # Verify
        model = self.env[self._test_model]
        result = model.search([(test_loader.identifier, "=", partner_name)])
        assert result["phone"] == updated_phone

    def test_not_update_record(self):

        # Setup
        partner_name = "partner_y"
        old_phone = "0167771"
        updated_phone = "010110"

        test_loader = BaseModelLoader()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"
        test_loader.update_existing_record = False

        test_loader.load_file([{"name": partner_name, "phone": old_phone}])

        # Replay
        test_loader.load_file([{"name": partner_name, "phone": updated_phone}])

        # Verify
        model = self.env[self._test_model]
        result = model.search([(test_loader.identifier, "=", partner_name)])
        assert result["phone"] == old_phone

    def test_filter_applied(self):

        # Setup
        test_loader = BaseModelLoader()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"
        test_loader.filters = {"website": "example.com"}

        # Replay
        filtered_partners = test_loader._mapper(
            self._get_unfiltered_partners(), None, test_loader.filters
        )

        # Verify
        for partner in filtered_partners:
            assert partner.get("website") == "example.com"
