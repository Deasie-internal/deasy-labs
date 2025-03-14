# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetadataSuggestStandardizationParams"]


class MetadataSuggestStandardizationParams(TypedDict, total=False):
    description: Required[str]

    endpoint_manager_config: Required[object]

    output_type: Required[str]

    tag_name: Required[str]

    value_distribution: Required[Dict[str, float]]

    vector_db_config: Required[object]

    context: Optional[str]

    existing_categories: Optional[object]
