# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SecretGetResponse"]


class SecretGetResponse(BaseModel):
    secret: Optional[str] = None
