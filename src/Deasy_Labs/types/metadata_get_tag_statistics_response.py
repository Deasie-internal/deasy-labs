# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetadataGetTagStatisticsResponse", "TagStatistics", "TagStatisticsExtractionStats"]


class TagStatisticsExtractionStats(BaseModel):
    count: float

    percentage: float


class TagStatistics(BaseModel):
    extraction_stats: Dict[str, TagStatisticsExtractionStats]

    percentage_of_total: float

    total_files_with_tag: int

    value_distribution: Dict[str, Dict[str, float]]


class MetadataGetTagStatisticsResponse(BaseModel):
    tag_statistics: Dict[str, TagStatistics]

    total_files: int
