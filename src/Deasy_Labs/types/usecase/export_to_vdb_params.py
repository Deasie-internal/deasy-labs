# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportToVdbParams"]


class ExportToVdbParams(TypedDict, total=False):
    target_vector_db_config: Required[object]

    export_level: Literal["file", "chunk", "both"]

    export_tags: Iterable[object]

    ori_vector_db_config: Optional[object]

    usecase_id: Optional[str]
