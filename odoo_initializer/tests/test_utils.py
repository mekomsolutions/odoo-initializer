import odoo
from odoo import api

from ..utils.config import config
from ..utils.registry import registry

class TestUtils:

    def get_record(self, record_id, model_name):
        cr = registry.cursor
        env = registry.env
        cr.execute("SELECT res_id FROM ir_model_data WHERE name='" + record_id + "';")
        result = cr.dictfetchall()
        if result is []:
            return
        internal_id = result[0].get('res_id')
        model = env[model_name]
        return model.browse(internal_id).read()[0]
