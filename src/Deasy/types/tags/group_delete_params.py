# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GroupDeleteParams"]


class GroupDeleteParams(TypedDict, total=False):
    group_id: Required[str]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    delete_associated_tags: bool
