# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataGetDistributionsParams"]


class MetadataGetDistributionsParams(TypedDict, total=False):
    vector_db_config: Required[object]

    columns: Optional[List[str]]

    conditions_new: Optional["ConditionParam"]

    max_val_per_tag: Optional[int]

    node_condition: Optional[Iterable[TagConditionParam]]

    usecase_id: Optional[str]


from .condition_param import ConditionParam
