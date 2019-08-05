import logging

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

_logger = logging.getLogger(__name__)

_logger.info("start initialization process")

registered_loaders = [
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
    CompanyPropertyLoader,
]

for registered_loader in registered_loaders:
    loader = registered_loader()
    loader.load_()


_logger.info("initialization done")
