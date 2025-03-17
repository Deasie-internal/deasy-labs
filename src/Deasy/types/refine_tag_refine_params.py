# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RefineTagRefineParams", "TagToRefine"]


class RefineTagRefineParams(TypedDict, total=False):
    endpoint_manager_config: Required[object]

    tag_to_refine: Required[Dict[str, TagToRefine]]

    vector_db_config: Required[object]

    file_names: Optional[List[str]]


class TagToRefine(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    output_type: Required[str]

    available_values: Optional[List[str]]

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    date_format: Optional[str]

    examples: Optional[List[Union[str, object]]]

    max_values: Annotated[Union[int, str, Iterable[object], None], PropertyInfo(alias="maxValues")]

    neg_examples: Optional[List[str]]

    retry_feedback: Optional[object]

    tag_id: Optional[str]

    tuned: Optional[int]

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    username: Optional[str]
