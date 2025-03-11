# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataGetOobTagFileCountParams"]


class MetadataGetOobTagFileCountParams(TypedDict, total=False):
    vector_db_config: Required[object]

    conditions: Iterable[TagConditionParam]
