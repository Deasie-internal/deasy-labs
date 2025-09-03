# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["SchemaListParams"]


class SchemaListParams(TypedDict, total=False):
    schema_ids: Optional[SequenceNotStr[str]]
