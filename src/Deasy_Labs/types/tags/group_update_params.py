# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    group_id: Required[str]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    group_description: Optional[str]

    group_name: Optional[str]

    tag_ids: Optional[List[str]]
