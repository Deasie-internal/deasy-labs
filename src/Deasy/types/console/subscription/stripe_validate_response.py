# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["StripeValidateResponse"]


class StripeValidateResponse(BaseModel):
    is_active: bool

    message: str

    tier_id: str

    cancel_at_period_end: Optional[bool] = None

    period_end_date: Optional[datetime] = None
