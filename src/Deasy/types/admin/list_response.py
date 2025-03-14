# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ListResponse", "Token"]


class Token(BaseModel):
    created_at: datetime

    last_used: datetime

    status: str

    token_id: str

    username: str


class ListResponse(BaseModel):
    tokens: List[Token]
