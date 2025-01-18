from pydantic import BaseModel


class CryptoCloudStatsAmount(BaseModel):
    all: float
    created: float
    paid: float
    overpaid: float
    partial: float
    canceled: float
