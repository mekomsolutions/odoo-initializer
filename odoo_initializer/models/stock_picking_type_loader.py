from .base_loader import BaseLoader


class StockPickingTypeLoader(BaseLoader):
    model_name = "stock.picking.type"
    folder = "stock_picking_type"
    filters = {}
