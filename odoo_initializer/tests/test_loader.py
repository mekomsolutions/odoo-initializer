from odoo.tests import logging
from odoo import tests

_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(tests.BaseCase):
    def test_loader(self):
        import activator
