# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ContextualizeCreateResponse"]


class ContextualizeCreateResponse(BaseModel):
    completion_tokens: int

    embedding_tokens: int

    file_results: List[object]

    prompt_tokens: int
