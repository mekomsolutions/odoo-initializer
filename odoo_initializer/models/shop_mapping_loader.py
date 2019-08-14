from .base_csv_loader import BaseCsvLoader


class ShopMappingLoader(BaseCsvLoader):
    model_name = "order.type.shop.mapping"
    folder = "shop_mapping"
    filters = {}
