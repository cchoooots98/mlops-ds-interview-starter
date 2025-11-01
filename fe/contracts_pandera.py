# Placeholder for data/feature contracts
# You can implement Pandera or Pydantic models here. Example skeleton:
from typing import Optional
from pydantic import BaseModel, Field

class EventRow(BaseModel):
    user_id: int
    station_id: int
    ts: str  # ISO8601
    clicks_1h: int = Field(ge=0)
    clicks_24h: int = Field(ge=0)
    purchases_7d: int = Field(ge=0)
    y: int = Field(ge=0, le=1)
