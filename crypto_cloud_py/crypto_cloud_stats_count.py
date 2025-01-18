from pydantic import BaseModel


class CryptoCloudStatsCount(BaseModel):
    all: int
    created: int
    paid: int
    overpaid: int
    partial: int
    canceled: int
