# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    file_names: Required[List[str]]

    vector_db_config: Required[object]
