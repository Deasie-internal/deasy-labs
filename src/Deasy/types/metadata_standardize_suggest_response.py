# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["MetadataStandardizeSuggestResponse"]


class MetadataStandardizeSuggestResponse(BaseModel):
    standard_mapping: Dict[str, List[object]]
