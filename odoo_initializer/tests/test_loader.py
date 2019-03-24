from odoo.tests import logging
from odoo import tests

from ..models import BaseModelLoader

_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(tests.TransactionCase):

    _test_model = "res.partner"

    @staticmethod
    def _get_unfiltered_partners():
        return [
            {"name": "test_1", "website": "example.com"},
            {"name": "test_2", "website": "example.com"},
            {"name": "test_3", "website": "test.com"},
            {"name": "test_4", "website": "example.com"},
            {"name": "test_4", "website": "test.com"},
        ]

    def test_filter_applied(self):

        # Setup
        test_loader = BaseModelLoader()
        test_loader.model_name = self._test_model
        test_loader.identifier = "name"
        test_loader.test = True
        test_loader.filters = {"website": "example.com"}

        # Replay
        filtered_partners = test_loader._mapper(
            self._get_unfiltered_partners(), None, test_loader.filters
        )

        # Verify
        assert "test.com" not in filtered_partners
