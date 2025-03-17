# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetadataDeleteParams", "Condition"]


class MetadataDeleteParams(TypedDict, total=False):
    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    conditions: Optional[Iterable[Condition]]

    file_names: Optional[List[str]]

    tags: Optional[List[str]]


class Condition(TypedDict, total=False):
    tag_id: Required[str]

    operator: Optional[Literal["in", "not_in"]]

    values: Optional[List[str]]
