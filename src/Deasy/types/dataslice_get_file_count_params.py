# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasliceGetFileCountParams", "NewCondition", "NewConditionTag"]


class DatasliceGetFileCountParams(TypedDict, total=False):
    condition: Required[Iterable[object]]

    vector_db_config: Required[object]

    dataslice_id: Optional[str]

    new_condition: Optional[NewCondition]


class NewConditionTag(TypedDict, total=False):
    name: Required[str]

    values: Required[List[str]]


class NewCondition(TypedDict, total=False):
    children: Optional[Iterable[object]]

    condition: Optional[Literal["AND", "OR"]]

    tag: Optional[NewConditionTag]
