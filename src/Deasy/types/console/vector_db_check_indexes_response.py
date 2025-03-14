# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["VectorDBCheckIndexesResponse"]


class VectorDBCheckIndexesResponse(BaseModel):
    found_indexes: Optional[List[str]] = None

    missing_indexes: Optional[List[str]] = None

    total_indexes_found: Optional[int] = None
