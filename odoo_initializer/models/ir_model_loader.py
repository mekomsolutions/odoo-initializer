from .base_loader import BaseLoader


class IrModelLoader(BaseLoader):
    model_name = "ir.model"
    folder = "models"
    filters = {}
