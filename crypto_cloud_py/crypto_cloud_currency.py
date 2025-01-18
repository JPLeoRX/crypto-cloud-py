from pydantic import BaseModel
from crypto_cloud_py.crypto_cloud_network import CryptoCloudNetwork


class CryptoCloudCurrency(BaseModel):
    id: int
    code: str
    fullcode: str
    network: CryptoCloudNetwork
    name: str
    is_email_required: bool
    stablecoin: bool
    icon_base: str
    icon_network: str
    icon_qr: str
    order: int
