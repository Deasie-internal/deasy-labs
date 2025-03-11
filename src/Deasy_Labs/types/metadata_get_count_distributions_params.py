# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetadataGetCountDistributionsParams", "Condition"]


class MetadataGetCountDistributionsParams(TypedDict, total=False):
    current_tree: Required[str]

    vector_db_config: Required[object]

    conditions: Iterable[Condition]

    endpoint_manager_config: Optional[object]

    x_token: Annotated[str, PropertyInfo(alias="x-token")]


class Condition(TypedDict, total=False):
    tag_id: Required[str]

    values: Required[List[str]]
