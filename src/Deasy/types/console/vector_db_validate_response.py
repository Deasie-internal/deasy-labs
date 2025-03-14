# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VectorDBValidateResponse"]


class VectorDBValidateResponse(BaseModel):
    success: bool

    message: Optional[str] = None
