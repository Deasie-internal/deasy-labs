# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasliceCreateParams", "ConditionNew", "ConditionNewTag"]


class DatasliceCreateParams(TypedDict, total=False):
    dataslice_name: Required[str]

    graph_id: Required[str]

    latest_graph: Required[object]

    vdb_profile_name: Required[str]

    condition: Optional[Iterable[object]]

    condition_new: Optional[ConditionNew]

    data_points: Optional[int]

    description: Optional[str]

    status: str


class ConditionNewTag(TypedDict, total=False):
    name: Required[str]

    values: Required[List[str]]


class ConditionNew(TypedDict, total=False):
    children: Optional[Iterable[object]]

    condition: Optional[Literal["AND", "OR"]]

    tag: Optional[ConditionNewTag]
