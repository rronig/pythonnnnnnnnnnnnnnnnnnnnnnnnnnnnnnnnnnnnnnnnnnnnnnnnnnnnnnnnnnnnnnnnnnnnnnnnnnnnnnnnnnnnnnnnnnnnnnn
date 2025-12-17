from pydantic import Base64Bytes, BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
