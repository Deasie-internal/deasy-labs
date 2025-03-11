# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["SuggestDescriptionCreateResponse"]


class SuggestDescriptionCreateResponse(BaseModel):
    message: str

    status_code: int

    suggestion: str
