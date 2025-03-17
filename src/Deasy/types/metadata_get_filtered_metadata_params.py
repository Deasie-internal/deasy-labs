# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataGetFilteredMetadataParams", "Condition", "ConditionsNew", "ConditionsNewTag"]


class MetadataGetFilteredMetadataParams(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]

    vector_db_config: Required[object]

    conditions_new: Optional[ConditionsNew]

    dataslice_id: Optional[str]

    limit: Optional[int]

    node_condition: Optional[Iterable[TagConditionParam]]

    offset: Optional[int]

    search_query: Optional[str]


class Condition(TypedDict, total=False):
    tag_id: Required[str]

    values: Required[List[str]]


class ConditionsNewTag(TypedDict, total=False):
    name: Required[str]

    values: Required[List[str]]


class ConditionsNew(TypedDict, total=False):
    children: Optional[Iterable[object]]

    condition: Optional[Literal["AND", "OR"]]

    tag: Optional[ConditionsNewTag]
