# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["OcrSyncStatsParams"]


class OcrSyncStatsParams(TypedDict, total=False):
    data_source_manager_configs: Required[Iterable[object]]

    use_cache: Optional[bool]
