# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

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
from ...types.metadata import chunk_list_params
from ...types.metadata.chunk_list_response import ChunkListResponse

__all__ = ["ChunkResource", "AsyncChunkResource"]


class ChunkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChunkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return ChunkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChunkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return ChunkResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata_keys: Optional[List[str]] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChunkListResponse:
        """
        Get metadata for specified files and tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/metadata/chunk/list",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                    "metadata_keys": metadata_keys,
                    "search_query": search_query,
                },
                chunk_list_params.ChunkListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChunkListResponse,
        )


class AsyncChunkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChunkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncChunkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChunkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncChunkResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata_keys: Optional[List[str]] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChunkListResponse:
        """
        Get metadata for specified files and tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/metadata/chunk/list",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                    "metadata_keys": metadata_keys,
                    "search_query": search_query,
                },
                chunk_list_params.ChunkListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChunkListResponse,
        )


class ChunkResourceWithRawResponse:
    def __init__(self, chunk: ChunkResource) -> None:
        self._chunk = chunk

        self.list = to_raw_response_wrapper(
            chunk.list,
        )


class AsyncChunkResourceWithRawResponse:
    def __init__(self, chunk: AsyncChunkResource) -> None:
        self._chunk = chunk

        self.list = async_to_raw_response_wrapper(
            chunk.list,
        )


class ChunkResourceWithStreamingResponse:
    def __init__(self, chunk: ChunkResource) -> None:
        self._chunk = chunk

        self.list = to_streamed_response_wrapper(
            chunk.list,
        )


class AsyncChunkResourceWithStreamingResponse:
    def __init__(self, chunk: AsyncChunkResource) -> None:
        self._chunk = chunk

        self.list = async_to_streamed_response_wrapper(
            chunk.list,
        )
