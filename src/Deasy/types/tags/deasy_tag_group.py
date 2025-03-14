# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DeasyTagGroup"]


class DeasyTagGroup(BaseModel):
    group_id: str

    username: str

    description: Optional[str] = None

    name: Optional[str] = None

    tag_ids: Optional[List[str]] = None
