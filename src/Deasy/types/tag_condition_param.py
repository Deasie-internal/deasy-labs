# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TagConditionParam"]


class TagConditionParam(TypedDict, total=False):
    tag_id: Required[str]

    operator: Optional[Literal["in", "not_in"]]

    values: Optional[List[str]]
