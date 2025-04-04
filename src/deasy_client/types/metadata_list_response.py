# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "MetadataListResponse",
    "MetadataMetadataItem",
    "MetadataMetadataItemChunkLevel",
    "MetadataMetadataItemFileLevel",
]


class MetadataMetadataItemChunkLevel(BaseModel):
    values: List[str]

    evidence: Optional[str] = None


class MetadataMetadataItemFileLevel(BaseModel):
    values: List[str]

    evidence: Optional[str] = None


class MetadataMetadataItem(BaseModel):
    chunk_level: Optional[Dict[str, Optional[MetadataMetadataItemChunkLevel]]] = None

    file_level: Optional[MetadataMetadataItemFileLevel] = None


class MetadataListResponse(BaseModel):
    metadata: Dict[str, Dict[str, MetadataMetadataItem]]
