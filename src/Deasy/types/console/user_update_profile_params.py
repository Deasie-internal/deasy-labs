# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserUpdateProfileParams"]


class UserUpdateProfileParams(TypedDict, total=False):
    company: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    phone_number: Required[str]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]
