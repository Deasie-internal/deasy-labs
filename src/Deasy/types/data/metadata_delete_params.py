# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MetadataDeleteParams"]


class MetadataDeleteParams(TypedDict, total=False):
    file_names: Required[List[str]]

    metadata_keys: Required[List[str]]

    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    limit: Optional[int]
