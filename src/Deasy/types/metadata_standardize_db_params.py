# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MetadataStandardizeDBParams"]


class MetadataStandardizeDBParams(TypedDict, total=False):
    endpoint_manager_config: Required[object]

    standard_mapping: Required[Dict[str, Iterable[object]]]

    tag_name: Required[str]

    vector_db_config: Required[object]
