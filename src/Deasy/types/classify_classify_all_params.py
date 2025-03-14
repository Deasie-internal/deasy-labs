# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClassifyClassifyAllParams", "Tags"]


class ClassifyClassifyAllParams(TypedDict, total=False):
    endpoint_manager_config: Required[object]

    vector_db_config: Required[object]

    conditions: Optional[Iterable[object]]

    dataslice_id: Optional[str]

    generate_file_tags: bool

    hierarchy: Optional[object]

    job_id: Optional[str]

    llm_dry_run: bool

    overwrite: bool

    soft_run: bool

    tags: Optional[Dict[str, Tags]]

    total_data_sets: int


class Tags(TypedDict, total=False):
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
