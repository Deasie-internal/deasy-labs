# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["DatasliceTagVdbDistributionResponse"]


class DatasliceTagVdbDistributionResponse(BaseModel):
    tag_distribution: Dict[str, int]
