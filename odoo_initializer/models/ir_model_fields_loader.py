from .base_loader import BaseLoader


class IrModelFieldsLoader(BaseLoader):
    model_name = "ir.model.fields"
    folder = "custom_fields"
    filters = {}
