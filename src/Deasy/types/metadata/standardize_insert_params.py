# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["StandardizeInsertParams"]


class StandardizeInsertParams(TypedDict, total=False):
    standard_mapping: Required[object]

    tag_id: Required[str]

    tag_name: Required[str]

    vector_db_config: Required[object]

    taxonomy_name: Optional[str]
