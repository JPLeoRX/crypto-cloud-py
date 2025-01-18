from typing import Optional
from pydantic import BaseModel
from crypto_cloud_py.crypto_cloud_currency import CryptoCloudCurrency
from crypto_cloud_py.crypto_cloud_project import CryptoCloudProject


class CryptoCloudInvoiceInfo(BaseModel):
    uuid: str
    address: str
    expiry_date: str
    side_commission: Optional[str] = None
    side_commission_cc: Optional[str] = None
    amount: float
    amount_usd: float
    received: float
    received_usd: float
    fee: float
    fee_usd: float
    service_fee: float
    service_fee_usd: float
    status: str
    order_id: str
    currency: CryptoCloudCurrency
    project: CryptoCloudProject
    test_mode: bool
