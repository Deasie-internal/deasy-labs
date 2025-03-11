# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["VdbconnectorGetDeleteStatsResponse"]


class VdbconnectorGetDeleteStatsResponse(BaseModel):
    file_count_with_vdb: int

    usecases_for_vdb: List[str]
