# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UsecaseCheckSyncParams"]


class UsecaseCheckSyncParams(TypedDict, total=False):
    hard_limit: Optional[int]

    usecase_id: Optional[str]

    vector_db_config: Optional[object]
