# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetadataGetDistinctValuesParams"]


class MetadataGetDistinctValuesParams(TypedDict, total=False):
    page: Required[int]

    tag_id: Required[str]

    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    conditions: Optional[Iterable[object]]

    per_page: Optional[int]

    search_query: Optional[str]
