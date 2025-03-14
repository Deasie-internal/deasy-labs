# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ConsoleFetchTiersResponse", "Tier"]


class Tier(BaseModel):
    max_tags_created_limit: int

    max_tags_stored_limit: int

    tier_id: str

    monthly_fee: Optional[int] = None


class ConsoleFetchTiersResponse(BaseModel):
    tiers: List[Tier]
