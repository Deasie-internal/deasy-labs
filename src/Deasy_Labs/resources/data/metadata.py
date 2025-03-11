# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

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
from ...types.data import metadata_list_params, metadata_delete_params
from ..._base_client import make_request_options
from ...types.data.metadata_list_response import MetadataListResponse
from ...types.data.metadata_delete_response import MetadataDeleteResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        full_text_filters: Optional[List[str]] | NotGiven = NOT_GIVEN,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        metadata_key_filters: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata_keys: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata_value_filters: Optional[Dict[str, List[str]]] | NotGiven = NOT_GIVEN,
        point_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataListResponse:
        """
        Retrieve metadata for specified files or nodes in vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/data/metadata/list",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                    "full_text_filters": full_text_filters,
                    "group_by": group_by,
                    "limit": limit,
                    "metadata_key_filters": metadata_key_filters,
                    "metadata_keys": metadata_keys,
                    "metadata_value_filters": metadata_value_filters,
                    "point_ids": point_ids,
                },
                metadata_list_params.MetadataListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListResponse,
        )

    def delete(
        self,
        *,
        file_names: List[str],
        metadata_keys: List[str],
        vector_db_config: object,
        x_user: str,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataDeleteResponse:
        """
        Delete specified metadata entries in vector database for given files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/data/metadata/delete",
            body=maybe_transform(
                {
                    "file_names": file_names,
                    "metadata_keys": metadata_keys,
                    "vector_db_config": vector_db_config,
                    "limit": limit,
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

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        full_text_filters: Optional[List[str]] | NotGiven = NOT_GIVEN,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        metadata_key_filters: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata_keys: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata_value_filters: Optional[Dict[str, List[str]]] | NotGiven = NOT_GIVEN,
        point_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataListResponse:
        """
        Retrieve metadata for specified files or nodes in vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/data/metadata/list",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                    "full_text_filters": full_text_filters,
                    "group_by": group_by,
                    "limit": limit,
                    "metadata_key_filters": metadata_key_filters,
                    "metadata_keys": metadata_keys,
                    "metadata_value_filters": metadata_value_filters,
                    "point_ids": point_ids,
                },
                metadata_list_params.MetadataListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListResponse,
        )

    async def delete(
        self,
        *,
        file_names: List[str],
        metadata_keys: List[str],
        vector_db_config: object,
        x_user: str,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataDeleteResponse:
        """
        Delete specified metadata entries in vector database for given files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/data/metadata/delete",
            body=await async_maybe_transform(
                {
                    "file_names": file_names,
                    "metadata_keys": metadata_keys,
                    "vector_db_config": vector_db_config,
                    "limit": limit,
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

        self.list = to_raw_response_wrapper(
            metadata.list,
        )
        self.delete = to_raw_response_wrapper(
            metadata.delete,
        )


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.list = async_to_raw_response_wrapper(
            metadata.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metadata.delete,
        )


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.list = to_streamed_response_wrapper(
            metadata.list,
        )
        self.delete = to_streamed_response_wrapper(
            metadata.delete,
        )


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.list = async_to_streamed_response_wrapper(
            metadata.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metadata.delete,
        )
