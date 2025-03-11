# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GenerateFileTagCreateParams"]


class GenerateFileTagCreateParams(TypedDict, total=False):
    endpoint_manager_config: Required[object]

    file_names: Required[List[str]]

    tags: Required[Optional[Dict[str, object]]]

    vector_db_config: Required[object]

    job_id: Optional[str]

    usecase_id: Optional[str]
