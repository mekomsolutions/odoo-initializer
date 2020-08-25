from .base_loader import BaseLoader


class SyncableUnitsLoader(BaseLoader):
    model_name = "syncable.units"
    folder = "syncable_units"
    filters = {}
