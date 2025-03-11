# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["GraphCreateOrUpdateParams"]


class GraphCreateOrUpdateParams(TypedDict, total=False):
    graph_data: Optional[object]

    graph_description: Optional[str]

    graph_id: Optional[str]

    graph_name: Optional[str]
