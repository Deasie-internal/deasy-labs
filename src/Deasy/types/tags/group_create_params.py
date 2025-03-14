# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    group_name: Required[str]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    group_description: str

    tag_ids: List[str]
