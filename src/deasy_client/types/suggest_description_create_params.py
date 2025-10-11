# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SuggestDescriptionCreateParams"]


class SuggestDescriptionCreateParams(TypedDict, total=False):
    data_connector_name: Required[str]

    tag_name: Required[str]

    available_values: Optional[SequenceNotStr[str]]

    context: Optional[str]

    current_description: Optional[str]

    dataslice_id: Optional[str]

    llm_profile_name: Optional[str]
