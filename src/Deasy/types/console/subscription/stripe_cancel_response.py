# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["StripeCancelResponse"]


class StripeCancelResponse(BaseModel):
    message: str

    period_end_date: datetime
