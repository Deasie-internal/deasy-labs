# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["DataListPaginatedResponse"]


class DataListPaginatedResponse(BaseModel):
    entities: List[str]

    error_message: Optional[str] = None

    next_offset: Optional[object] = None
