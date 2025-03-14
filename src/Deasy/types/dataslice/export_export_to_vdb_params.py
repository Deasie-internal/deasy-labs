# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportExportToVdbParams"]


class ExportExportToVdbParams(TypedDict, total=False):
    target_vector_db_config: Required[object]

    dataslice_id: Optional[str]

    export_level: Literal["file", "chunk", "both"]

    export_tags: Iterable[object]

    ori_vector_db_config: Optional[object]
