# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GraphUpsertParams"]


class GraphUpsertParams(TypedDict, total=False):
    graph_name: Required[str]

    graph_data: Optional[object]

    graph_description: Optional[str]

    new_graph_name: Optional[str]
