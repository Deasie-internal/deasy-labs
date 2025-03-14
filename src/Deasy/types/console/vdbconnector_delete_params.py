# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VdbconnectorDeleteParams"]


class VdbconnectorDeleteParams(TypedDict, total=False):
    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]
