# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasliceGetFileCountParams"]


class DatasliceGetFileCountParams(TypedDict, total=False):
    condition: Required[Iterable[object]]

    vector_db_config: Required[object]

    dataslice_id: Optional[str]

    new_condition: Optional["ConditionParam"]


from .condition_param import ConditionParam
