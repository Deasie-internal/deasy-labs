# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataGetDistributionsParams", "ConditionsNew", "ConditionsNewTag"]


class MetadataGetDistributionsParams(TypedDict, total=False):
    vector_db_config: Required[object]

    columns: Optional[List[str]]

    conditions_new: Optional[ConditionsNew]

    dataslice_id: Optional[str]

    max_val_per_tag: Optional[int]

    node_condition: Optional[Iterable[TagConditionParam]]


class ConditionsNewTag(TypedDict, total=False):
    name: Required[str]

    values: Required[List[str]]


class ConditionsNew(TypedDict, total=False):
    children: Optional[Iterable[object]]

    condition: Optional[Literal["AND", "OR"]]

    tag: Optional[ConditionsNewTag]
