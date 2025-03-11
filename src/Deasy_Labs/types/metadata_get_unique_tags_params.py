# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataGetUniqueTagsParams"]


class MetadataGetUniqueTagsParams(TypedDict, total=False):
    vector_db_config: Required[object]

    file_names: Optional[List[str]]

    node_condition: Optional[Iterable[TagConditionParam]]

    usecase_id: Optional[str]
