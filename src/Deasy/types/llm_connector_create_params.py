# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .openai_config_param import OpenAIConfigParam
from .deasy_compute_config_param import DeasyComputeConfigParam

__all__ = ["LlmConnectorCreateParams", "ConnectorBody"]


class LlmConnectorCreateParams(TypedDict, total=False):
    connector_body: Required[ConnectorBody]

    connector_name: Required[str]


ConnectorBody: TypeAlias = Union[DeasyComputeConfigParam, OpenAIConfigParam]
