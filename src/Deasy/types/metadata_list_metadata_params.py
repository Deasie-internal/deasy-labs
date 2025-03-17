# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetadataListMetadataParams"]


class MetadataListMetadataParams(TypedDict, total=False):
    vector_db_config: Required[object]

    conditions: Optional["ConditionInputParam"]

    dataslice_id: Optional[str]

    include_chunk_level: Optional[bool]

    tag_names: Optional[List[str]]


from .condition_input_param import ConditionInputParam
