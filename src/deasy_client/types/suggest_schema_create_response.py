# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SuggestSchemaCreateResponse", "SuggestedTags"]


class SuggestedTags(BaseModel):
    name: str

    output_type: str

    available_values: Optional[List[str]] = None

    date_format: Optional[str] = None

    description: Optional[str] = None

    examples: Optional[List[Union[Dict[str, object], str]]] = None

    max_values: Optional[int] = FieldInfo(alias="maxValues", default=None)

    tag_id: Optional[str] = None

    tuned: Optional[int] = None


class SuggestSchemaCreateResponse(BaseModel):
    suggestion: Dict[str, object]

    message: Optional[str] = None

    status_code: Optional[int] = None

    suggested_tags: Optional[Dict[str, SuggestedTags]] = None
