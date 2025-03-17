# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["TagTextClassifyResponse"]


class TagTextClassifyResponse(BaseModel):
    completion_tokens: int

    embedding_tokens: int

    prompt_tokens: int

    tags: object
