# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DatasliceListResponse", "Dataslice", "DatasliceConditionNew", "DatasliceConditionNewTag"]


class DatasliceConditionNewTag(BaseModel):
    name: str

    values: List[str]


class DatasliceConditionNew(BaseModel):
    children: Optional[List[object]] = None

    condition: Optional[Literal["AND", "OR"]] = None

    tag: Optional[DatasliceConditionNewTag] = None


class Dataslice(BaseModel):
    data_points: int

    dataslice_id: str

    dataslice_name: str

    last_updated: datetime

    status: str

    condition: Optional[List[object]] = None

    condition_new: Optional[DatasliceConditionNew] = None

    description: Optional[str] = None

    export_collection_name: Optional[str] = None

    graph_id: Optional[str] = None

    latest_graph: Optional[object] = None

    vector_db_config: Optional[object] = None


class DatasliceListResponse(BaseModel):
    dataslices: List[Dataslice]
