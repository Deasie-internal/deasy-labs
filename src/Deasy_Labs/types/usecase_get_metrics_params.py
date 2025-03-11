# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["UsecaseGetMetricsParams"]


class UsecaseGetMetricsParams(TypedDict, total=False):
    file_names: Optional[List[str]]

    node_ids: Optional[List[str]]

    tags: Optional[List[str]]

    usecase_id: Optional[str]

    vector_db_config: Optional[object]
