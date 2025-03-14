# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DatasliceCreateParams"]


class DatasliceCreateParams(TypedDict, total=False):
    condition: Required[Iterable[object]]

    data_points: Required[int]

    dataslice_id: Required[str]

    dataslice_name: Required[str]

    description: Required[str]

    graph_id: Required[str]

    last_updated: Required[str]

    latest_graph: Required[object]

    status: Required[str]

    user_id: Required[str]

    vector_db_config: Required[object]

    condition_new: "ConditionParam"


from .condition_param import ConditionParam
