# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["DataGetDocumentTextResponse"]


class DataGetDocumentTextResponse(BaseModel):
    text_data: Dict[str, str]
