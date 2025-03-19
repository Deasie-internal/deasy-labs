# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PrepareDataCreateParams"]


class PrepareDataCreateParams(TypedDict, total=False):
    vdb_profile_name: Required[str]

    llm_profile_name: Optional[str]

    total_data_sets: Optional[int]
