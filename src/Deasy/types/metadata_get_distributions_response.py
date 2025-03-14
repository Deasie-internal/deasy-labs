# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetadataGetDistributionsResponse"]


class MetadataGetDistributionsResponse(BaseModel):
    distributions: Dict[str, Dict[str, int]]

    filename_count: int
