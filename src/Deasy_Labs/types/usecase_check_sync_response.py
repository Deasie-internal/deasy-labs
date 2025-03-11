# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["UsecaseCheckSyncResponse"]


class UsecaseCheckSyncResponse(BaseModel):
    deasy_sync_percentage: float

    tag_counters: Dict[str, List[int]]
