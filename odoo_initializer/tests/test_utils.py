import odoo
from odoo import api

from ..utils.config import config


class TestUtils:

    def get_record(self, record_id, model_name):
        with api.Environment.manage():
            registry = odoo.registry(config.db_name)
            with registry.cursor() as cr:
                cr.execute("SELECT res_id FROM ir_model_data WHERE name='" + record_id + "';")
                result = cr.dictfetchall()
                if result is []:
                    return
                internal_id = result[0].get('res_id')
                uid = odoo.SUPERUSER_ID
                env = odoo.api.Environment(cr, uid, {})
                model = env[model_name]
                return model.browse(internal_id).read()[0]
