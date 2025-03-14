# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataFilterByConditionsParams"]


class MetadataFilterByConditionsParams(TypedDict, total=False):
    conditions: Required[Iterable[TagConditionParam]]

    vector_db_config: Required[object]

    analyze_remaining_tags: Optional[List[str]]
