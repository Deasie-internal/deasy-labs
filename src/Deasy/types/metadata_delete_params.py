# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetadataDeleteParams"]


class MetadataDeleteParams(TypedDict, total=False):
    vdb_profile_name: Required[str]

    x_user: Required[Annotated[str, PropertyInfo(alias="x-user")]]

    conditions: Optional["ConditionInputParam"]

    file_names: Optional[List[str]]

    tags: Optional[List[str]]


from .condition_input_param import ConditionInputParam
