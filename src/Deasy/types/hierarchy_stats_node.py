# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["HierarchyStatsNode"]


class HierarchyStatsNode(BaseModel):
    file_count: int

    name: str

    children: Optional[List["HierarchyStatsNode"]] = None

    percentage: Optional[float] = None


if PYDANTIC_V2:
    HierarchyStatsNode.model_rebuild()
else:
    HierarchyStatsNode.update_forward_refs()  # type: ignore
