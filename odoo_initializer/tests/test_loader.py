from odoo.tests import logging
from odoo import tests

from ..models import BaseModelImporter

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

    def test_no_duplicates(self):

        # Setup
        test_loader = BaseModelImporter()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"

        # Replay
        test_loader.load_file(self._get_duplicate_partners())

        # Verify
        model = self.env[self._test_model]
        result = model.search(
                        [(test_loader.identifier, "=", "partner_1")]
                    )

        # Assert that only one record is created per identifier
        assert len(result) == 1, "a duplicate record was found."

    def test_update_record(self):

        # Setup
        partner_name = "partner_x"
        old_phone = "0167771"
        updated_phone = "010110"

        test_loader = BaseModelImporter()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"
        test_loader.update_existing_record = True

        test_loader.load_file([{"name": partner_name, "phone": old_phone}])

        # Replay
        test_loader.load_file([{"name": partner_name, "phone": updated_phone}])

        # Verify
        model = self.env[self._test_model]
        result = model.search(
            [(test_loader.identifier, "=", partner_name)]
        )
        assert result["phone"] == updated_phone

    def test_not_update_record(self):

        # Setup
        partner_name = "partner_y"
        old_phone = "0167771"
        updated_phone = "010110"

        test_loader = BaseModelImporter()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"
        test_loader.update_existing_record = False

        test_loader.load_file([{"name": partner_name, "phone": old_phone}])

        # Replay
        test_loader.load_file([{"name": partner_name, "phone": updated_phone}])

        # Verify
        model = self.env[self._test_model]
        result = model.search(
            [(test_loader.identifier, "=", partner_name)]
        )
        assert result["phone"] == old_phone
