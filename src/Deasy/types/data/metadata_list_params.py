# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MetadataListParams"]


class MetadataListParams(TypedDict, total=False):
    vector_db_config: Required[object]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    file_names: Optional[List[str]]

    full_text_filters: Optional[List[str]]

    group_by: Optional[str]

    limit: Optional[int]

    metadata_key_filters: Optional[List[str]]

    metadata_keys: Optional[List[str]]

    metadata_value_filters: Optional[Dict[str, List[str]]]

    point_ids: Optional[List[str]]
