# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["StandardizeTagDistributionResponse"]


class StandardizeTagDistributionResponse(BaseModel):
    tag_distribution: Dict[str, Dict[str, float]]

    unique_tag_count: int
