from odoo.tests import logging
from odoo import tests
from models.drug_loader import DrugLoader


_logger = logging.getLogger(__name__)


class TestOpenmrsLoader(tests.BaseCase):
    def test_drug_loader(self):
        drug_loader = DrugLoader()
        drug_loader.load_()
