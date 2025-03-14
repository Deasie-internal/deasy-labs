# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProgressTrackerRetrieveTaskStatusResponse"]


class ProgressTrackerRetrieveTaskStatusResponse(BaseModel):
    completed_progress_increments: int

    status: Literal["in_progress", "completed", "aborted", "failed"]

    total_progress_increments: int

    tags_created: Optional[int] = None
