# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetadataGetEvidenceResponse"]


class MetadataGetEvidenceResponse(BaseModel):
    evidence: Dict[str, str]
