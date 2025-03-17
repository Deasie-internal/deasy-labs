# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["GroupDeleteResponse"]


class GroupDeleteResponse(BaseModel):
    message: str

    failed_tags: Optional[List[str]] = None

    success: Optional[bool] = None

    successful_tags: Optional[Dict[str, str]] = None
