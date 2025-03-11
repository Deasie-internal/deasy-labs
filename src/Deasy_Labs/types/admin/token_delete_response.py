# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["TokenDeleteResponse"]


class TokenDeleteResponse(BaseModel):
    message: str

    token_id: str
