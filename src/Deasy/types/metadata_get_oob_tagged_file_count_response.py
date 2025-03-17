# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetadataGetOobTaggedFileCountResponse"]


class MetadataGetOobTaggedFileCountResponse(BaseModel):
    fully_tagged_files: int

    oob_tag_counts: Dict[str, int]
