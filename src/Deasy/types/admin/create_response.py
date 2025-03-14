# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["CreateResponse"]


class CreateResponse(BaseModel):
    token_id: str

    token_value: str

    username: str
