# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "MetadataListMetadataResponse",
    "MetadataMetadataItem",
    "MetadataMetadataItemChunkLevel",
    "MetadataMetadataItemFileLevel",
]


class MetadataMetadataItemChunkLevel(BaseModel):
    evidence: str

    values: List[str]


class MetadataMetadataItemFileLevel(BaseModel):
    evidence: str

    values: List[str]


class MetadataMetadataItem(BaseModel):
    chunk_level: Optional[Dict[str, Optional[MetadataMetadataItemChunkLevel]]] = None

    file_level: Optional[MetadataMetadataItemFileLevel] = None


class MetadataListMetadataResponse(BaseModel):
    metadata: Dict[str, Dict[str, MetadataMetadataItem]]
