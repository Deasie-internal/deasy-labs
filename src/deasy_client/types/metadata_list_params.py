# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MetadataListParams"]


class MetadataListParams(TypedDict, total=False):
    data_connector_name: Required[str]

    chunk_ids: Optional[SequenceNotStr[str]]

    conditions: Optional["ConditionInputParam"]

    dataslice_id: Optional[str]

    file_names: Optional[SequenceNotStr[str]]

    include_chunk_level: Optional[bool]

    tag_names: Optional[SequenceNotStr[str]]


from .condition_input_param import ConditionInputParam
