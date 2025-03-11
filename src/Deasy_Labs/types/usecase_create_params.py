# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UsecaseCreateParams"]


class UsecaseCreateParams(TypedDict, total=False):
    condition: Required[Iterable[object]]

    data_points: Required[int]

    description: Required[str]

    graph_id: Required[str]

    last_updated: Required[str]

    latest_graph: Required[object]

    status: Required[str]

    usecase_id: Required[str]

    usecase_name: Required[str]

    user_id: Required[str]

    vector_db_config: Required[object]

    condition_new: "ConditionParam"


from .condition_param import ConditionParam
