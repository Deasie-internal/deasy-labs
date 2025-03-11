# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["UsecaseGetFileCountParams"]


class UsecaseGetFileCountParams(TypedDict, total=False):
    condition: Required[Iterable[object]]

    vector_db_config: Required[object]

    new_condition: Optional["ConditionParam"]

    usecase_id: Optional[str]


from .condition_param import ConditionParam
