# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .deasy_tag_group import DeasyTagGroup

__all__ = ["GroupListResponse"]


class GroupListResponse(BaseModel):
    tag_groups: List[DeasyTagGroup]
