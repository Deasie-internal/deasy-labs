# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DocumentTextGetParams"]


class DocumentTextGetParams(TypedDict, total=False):
    data_connector_name: Required[str]

    file_names: Required[SequenceNotStr[str]]

    chunk_ids: Optional[SequenceNotStr[str]]
