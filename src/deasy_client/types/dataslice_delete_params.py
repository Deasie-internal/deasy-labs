# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasliceDeleteParams"]


class DatasliceDeleteParams(TypedDict, total=False):
    dataslice_id: Required[str]
