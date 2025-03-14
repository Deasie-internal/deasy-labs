# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["UserUpdateProfileResponse"]


class UserUpdateProfileResponse(BaseModel):
    message: str

    success: bool
