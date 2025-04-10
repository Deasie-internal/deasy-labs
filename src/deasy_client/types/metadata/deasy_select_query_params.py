# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "DeasySelectQueryParams",
    "TagDistributions",
    "TagDistributionsData",
    "TagDistributionsDataValues",
    "TagSchema",
]


class DeasySelectQueryParams(TypedDict, total=False):
    query: Required[str]

    vdb_profile_name: Required[str]

    max_filter_values_to_choose: Optional[int]

    max_filters_to_choose: Optional[int]

    max_results: Optional[int]

    max_search_reduction: Optional[float]

    min_filter_values_to_choose: Optional[int]

    min_filters_to_choose: Optional[int]

    min_search_reduction: Optional[float]

    query_type: Optional[Literal["sql", "deasy"]]

    return_only_query: Optional[bool]

    return_type: Optional[Literal["results", "condition", "both"]]

    tag_distributions: Optional[TagDistributions]
    """Complete tag distribution data structure for analyzing filter impacts.

    Maps field names to their value distributions. Used for estimating search
    reductions without executing filters.
    """

    tag_names: Optional[List[str]]

    tag_schemas: Optional[Iterable[TagSchema]]


class TagDistributionsDataValues(TypedDict, total=False):
    file_count: Required[int]

    chunk_count: Optional[int]

    percentage: Optional[float]


class TagDistributionsData(TypedDict, total=False):
    values: Required[Dict[str, TagDistributionsDataValues]]

    coverage_percentage: Optional[float]

    total_count: Optional[int]


class TagDistributions(TypedDict, total=False):
    data: Dict[str, TagDistributionsData]


class TagSchema(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    output_type: Required[str]

    available_values: Optional[List[str]]

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    date_format: Optional[str]

    examples: Optional[List[Union[str, Dict[str, object]]]]

    max_values: Annotated[Union[int, str, Iterable[object], None], PropertyInfo(alias="maxValues")]

    neg_examples: Optional[List[str]]

    retry_feedback: Optional[Dict[str, object]]

    tag_id: Optional[str]

    tuned: Optional[int]

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    username: Optional[str]
