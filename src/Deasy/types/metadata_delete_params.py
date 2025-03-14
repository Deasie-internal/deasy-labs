# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tag_condition_param import TagConditionParam

__all__ = ["MetadataDeleteParams"]


class MetadataDeleteParams(TypedDict, total=False):
    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    conditions: Optional[Iterable[TagConditionParam]]

    file_names: Optional[List[str]]

    tags: Optional[List[str]]
