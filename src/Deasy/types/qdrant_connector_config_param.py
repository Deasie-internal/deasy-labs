# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QdrantConnectorConfigParam", "IndexInfo"]


class IndexInfo(TypedDict, total=False):
    total_indexes_found: Required[int]


class QdrantConnectorConfigParam(TypedDict, total=False):
    api_key: Required[str]

    collection_name: Required[str]

    index_info: Required[IndexInfo]

    name: Required[str]

    url: Required[str]

    filename_key: str

    text_key: str

    type: str
