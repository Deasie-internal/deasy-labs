# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasliceGetMetricsParams"]


class DatasliceGetMetricsParams(TypedDict, total=False):
    data_connector_name: Optional[str]

    dataslice_id: Optional[str]

    file_names: Optional[SequenceNotStr[str]]

    node_ids: Optional[SequenceNotStr[str]]

    tags: Optional[SequenceNotStr[str]]
