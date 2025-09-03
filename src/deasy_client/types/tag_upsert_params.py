# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TagUpsertParams", "TagData"]


class TagUpsertParams(TypedDict, total=False):
    tag_data: Required[TagData]


class TagData(TypedDict, total=False):
    name: Required[str]

    output_type: Required[str]

    available_values: Optional[SequenceNotStr[str]]

    date_format: Optional[str]

    description: Optional[str]

    enhance_file_metadata: Optional[bool]

    examples: Optional[SequenceNotStr[Union[str, Dict[str, object]]]]

    max_values: Annotated[Optional[int], PropertyInfo(alias="maxValues")]

    tag_id: Optional[str]

    tuned: Optional[int]
