# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PsqlConnectorConfigParam", "IndexInfo"]


class IndexInfo(TypedDict, total=False):
    found_indexes: Required[SequenceNotStr[str]]

    total_indexes_found: Required[int]


class PsqlConnectorConfigParam(TypedDict, total=False):
    collection_name: Required[str]

    database_name: Required[str]

    db_user: Required[str]

    name: Required[str]

    password: Required[str]

    port: Required[str]

    url: Required[str]

    filename_key: str

    index_info: Optional[IndexInfo]

    text_key: str

    type: Literal["PSQLVectorDBManager"]
