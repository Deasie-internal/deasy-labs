# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["DatasliceListResponse"]


class DatasliceListResponse(BaseModel):
    dataslices: List[object]

    message: str
