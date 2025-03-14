# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["MetadataFilterByConditionsResponse"]


class MetadataFilterByConditionsResponse(BaseModel):
    matched_count: int

    matched_files: List[str]

    remaining_tag_statistics: Dict[str, Dict[str, Dict[str, float]]]
