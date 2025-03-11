# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContextualizeCreateParams"]


class ContextualizeCreateParams(TypedDict, total=False):
    endpoint_manager_config: Required[object]

    vector_db_config: Required[object]

    file_names: Optional[List[str]]

    ignore_untagged_files: bool

    job_id: Optional[str]

    overwrite: bool

    usecase_id: Optional[str]

    verbose: bool
