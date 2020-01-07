from .base_loader import BaseLoader


class ShopMappingLoader(BaseLoader):
    model_name = "order.type.shop.mapping"
    folder = "shop_mapping"
    filters = {}
