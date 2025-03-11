# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetadataGetOobTagFileCountResponse"]


class MetadataGetOobTagFileCountResponse(BaseModel):
    fully_tagged_files: int

    oob_tag_counts: Dict[str, int]
