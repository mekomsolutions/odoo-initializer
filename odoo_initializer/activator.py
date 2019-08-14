import logging

from .models.country_loader import CountryLoader
from .models.partner_loader import PartnerLoader
from .models.company_loader import CompanyLoader
from .models.company_property_loader import CompanyPropertyLoader
from .models.stock_location_loader import StockLocationLoader
from .models.payment_term_loader import PaymentTermLoader
from .models.price_list_loader import PriceListLoader
from .models.account_loader import AccountLoader
from .models.journal_loader import JournalLoader
from .models.fiscal_position_loader import FiscalPositionLoader
from .models.sale_shop_loader import SaleShopLoader
from .models.drug_loader import DrugLoader
from .models.product_loader import ProductLoader
from .models.order_type_loader import OrderTypeLoader
from .models.shop_mapping_loader import ShopMappingLoader
from .models.system_parameter_loader import SystemParameterLoader
from .models.default_value_loader import DefaultValueLoader

_logger = logging.getLogger(__name__)

_logger.info("start initialization process")

registered_loaders = [
    CountryLoader,
    FiscalPositionLoader,
    PartnerLoader,
    CompanyLoader,
    AccountLoader,
    JournalLoader,
    PaymentTermLoader,
    StockLocationLoader,
    DrugLoader,
    ProductLoader,
    PriceListLoader,
    SaleShopLoader,
    OrderTypeLoader,
    ShopMappingLoader,
    DefaultValueLoader,
    CompanyPropertyLoader,
    SystemParameterLoader,
]

for registered_loader in registered_loaders:
    loader = registered_loader()
    loader.load_()


_logger.info("initialization done")
