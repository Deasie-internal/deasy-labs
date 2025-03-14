# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketplaceSignupParams"]


class MarketplaceSignupParams(TypedDict, total=False):
    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    company: Optional[str]

    first_name: Optional[str]

    last_name: Optional[str]

    marketplace_token: Optional[str]
