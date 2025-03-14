# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel
from .deasy_tag_group import DeasyTagGroup

__all__ = ["GroupCreateResponse"]


class GroupCreateResponse(BaseModel):
    tag_group: DeasyTagGroup
