# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StandardizeTagDistributionParams"]


class StandardizeTagDistributionParams(TypedDict, total=False):
    tag_id: Required[str]

    vector_db_config: Required[object]
