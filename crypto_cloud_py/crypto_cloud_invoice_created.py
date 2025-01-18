from typing import Optional
from pydantic import BaseModel
from crypto_cloud_py.crypto_cloud_currency import CryptoCloudCurrency
from crypto_cloud_py.crypto_cloud_project import CryptoCloudProject


class CryptoCloudInvoiceCreated(BaseModel):
    uuid: str
    created: str
    address: str
    expiry_date: str
    side_commission: Optional[str] = None
    side_commission_cc: Optional[str] = None
    amount: float
    amount_usd: float
    amount_in_fiat: float
    fee: float
    fee_usd: float
    service_fee: float
    service_fee_usd: float
    type_payments: str
    fiat_currency: str
    status: str
    is_email_required: bool
    link: str
    invoice_id: Optional[str] = None
    currency: CryptoCloudCurrency
    project: CryptoCloudProject
    test_mode: bool
