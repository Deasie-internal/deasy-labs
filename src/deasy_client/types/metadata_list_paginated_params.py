# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MetadataListPaginatedParams"]


class MetadataListPaginatedParams(TypedDict, total=False):
    data_connector_name: Required[str]

    conditions: Optional["ConditionInputParam"]

    dataslice_id: Optional[str]

    include_chunk_level: Optional[bool]

    limit: Optional[int]

    offset: Optional[int]

    tag_names: Optional[SequenceNotStr[str]]


from .condition_input_param import ConditionInputParam
