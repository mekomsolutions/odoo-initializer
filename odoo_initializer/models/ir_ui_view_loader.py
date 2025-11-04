from .base_loader import BaseLoader


class IrUiViewLoader(BaseLoader):
    model_name = "ir.ui.view"
    folder = "views"
    filters = {}
