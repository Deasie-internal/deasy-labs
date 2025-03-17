# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ...types import metadata_delete_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tag_condition_param import TagConditionParam
from ...types.metadata_delete_response import MetadataDeleteResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        conditions: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataDeleteResponse:
        """
        Delete metadata for specified files and tags from the chunk-level metadata table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/metadata/delete",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "file_names": file_names,
                    "tags": tags,
                },
                metadata_delete_params.MetadataDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataDeleteResponse,
        )


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        conditions: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataDeleteResponse:
        """
        Delete metadata for specified files and tags from the chunk-level metadata table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/metadata/delete",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "file_names": file_names,
                    "tags": tags,
                },
                metadata_delete_params.MetadataDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataDeleteResponse,
        )


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.delete = to_raw_response_wrapper(
            metadata.delete,
        )


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.delete = async_to_raw_response_wrapper(
            metadata.delete,
        )


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.delete = to_streamed_response_wrapper(
            metadata.delete,
        )


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.delete = async_to_streamed_response_wrapper(
            metadata.delete,
        )
