# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SuggestHierarchySuggestParams"]


class SuggestHierarchySuggestParams(TypedDict, total=False):
    condition: Required[object]

    endpoint_manager_config: Required[object]

    vector_db_config: Required[object]

    context: Optional[str]

    context_level: Optional[str]

    current_tree: Optional[object]

    file_names: Optional[List[str]]

    max_height: Optional[int]

    node: Optional[object]

    tag_type: Optional[str]

    total_files: Optional[int]

    use_existing_tags: Optional[bool]

    use_extracted_tags: Optional[bool]

    usecase_id: Optional[str]
