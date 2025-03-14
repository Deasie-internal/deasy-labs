# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["MetadataGetFilteredMetadataResponse"]


class MetadataGetFilteredMetadataResponse(BaseModel):
    metadata: Dict[str, object]

    next_offset: Optional[int] = None

    total_matches: int
