# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DatasliceCheckSyncScoreParams"]


class DatasliceCheckSyncScoreParams(TypedDict, total=False):
    dataslice_id: Optional[str]

    hard_limit: Optional[int]

    vector_db_config: Optional[object]
