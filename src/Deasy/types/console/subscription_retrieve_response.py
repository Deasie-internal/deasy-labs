# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SubscriptionRetrieveResponse"]


class SubscriptionRetrieveResponse(BaseModel):
    monthly_limit: int

    monthly_usage: int

    storage_limit: int

    storage_usage: int

    tier_id: str

    cancel_at_period_end: Optional[bool] = None

    company: Optional[str] = None

    deasy_verified: Optional[bool] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    period_end_date: Optional[datetime] = None

    phone_number: Optional[str] = None

    subscription_source: Optional[str] = None
