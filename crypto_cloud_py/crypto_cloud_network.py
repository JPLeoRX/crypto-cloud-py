from pydantic import BaseModel


class CryptoCloudNetwork(BaseModel):
    code: str
    id: int
    icon: str
    fullname: str
