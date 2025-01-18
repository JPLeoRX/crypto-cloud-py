from typing import Optional
from pydantic import BaseModel


class CryptoCloudProject(BaseModel):
    id: int
    name: str
    fail: str
    success: str
    logo: Optional[str] = None
