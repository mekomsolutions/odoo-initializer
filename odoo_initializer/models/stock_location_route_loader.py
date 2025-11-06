from .base_loader import BaseLoader


class StockLocationRouteLoader(BaseLoader):
    model_name = "stock.location.route"
    folder = "stock_location_route"
    filters = {}
