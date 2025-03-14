# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["MetadataGetBasicMetadataResponse"]


class MetadataGetBasicMetadataResponse(BaseModel):
    metadata: Dict[str, List[object]]
