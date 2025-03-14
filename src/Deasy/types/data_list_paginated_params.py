# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataListPaginatedParams"]


class DataListPaginatedParams(TypedDict, total=False):
    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    entities_already_scrolled: Optional[List[str]]

    group_by: str

    hard_limit: Optional[int]

    limit: int

    offset: Union[int, str]

    scroll_limit: Optional[int]

    search_query: Optional[str]
