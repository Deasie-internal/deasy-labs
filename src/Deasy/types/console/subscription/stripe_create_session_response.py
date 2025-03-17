# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["StripeCreateSessionResponse"]


class StripeCreateSessionResponse(BaseModel):
    operation: Literal["create", "upgrade", "downgrade", "resume"]

    session_id: str

    url: str
