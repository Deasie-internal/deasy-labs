# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["OcrIngestParams"]


class OcrIngestParams(TypedDict, total=False):
    data_source_manager_config: Required[object]

    clean_up_out_of_sync: bool

    endpoint_manager_config: Optional[object]

    file_count_to_run: Optional[int]

    file_names: Optional[List[str]]

    job_id: Optional[str]

    use_llm: bool
