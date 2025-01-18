from pydantic import BaseModel
from crypto_cloud_py.crypto_cloud_stats_amount import CryptoCloudStatsAmount
from crypto_cloud_py.crypto_cloud_stats_count import CryptoCloudStatsCount


class CryptoCloudStats(BaseModel):
    count: CryptoCloudStatsCount
    amount: CryptoCloudStatsAmount
