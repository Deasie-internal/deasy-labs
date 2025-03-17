# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

from .file import (
    FileResource,
    AsyncFileResource,
    FileResourceWithRawResponse,
    AsyncFileResourceWithRawResponse,
    FileResourceWithStreamingResponse,
    AsyncFileResourceWithStreamingResponse,
)
from .chunk import (
    ChunkResource,
    AsyncChunkResource,
    ChunkResourceWithRawResponse,
    AsyncChunkResourceWithRawResponse,
    ChunkResourceWithStreamingResponse,
    AsyncChunkResourceWithStreamingResponse,
)
from ...types import (
    metadata_delete_params,
    metadata_upsert_params,
    metadata_list_metadata_params,
    metadata_list_paginated_metadata_params,
)
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
from .standardize import (
    StandardizeResource,
    AsyncStandardizeResource,
    StandardizeResourceWithRawResponse,
    AsyncStandardizeResourceWithRawResponse,
    StandardizeResourceWithStreamingResponse,
    AsyncStandardizeResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.tag_condition_param import TagConditionParam
from ...types.condition_input_param import ConditionInputParam
from ...types.metadata_delete_response import MetadataDeleteResponse
from ...types.metadata_upsert_response import MetadataUpsertResponse
from ...types.metadata_list_metadata_response import MetadataListMetadataResponse
from ...types.metadata_list_paginated_metadata_response import MetadataListPaginatedMetadataResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def file(self) -> FileResource:
        return FileResource(self._client)

    @cached_property
    def chunk(self) -> ChunkResource:
        return ChunkResource(self._client)

    @cached_property
    def standardize(self) -> StandardizeResource:
        return StandardizeResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
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

    def list_metadata(
        self,
        *,
        vector_db_config: object,
        conditions: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        include_chunk_level: Optional[bool] | NotGiven = NOT_GIVEN,
        tag_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataListMetadataResponse:
        """
        Get paginated filtered metadata based on conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/list",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "tag_names": tag_names,
                },
                metadata_list_metadata_params.MetadataListMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListMetadataResponse,
        )

    def list_paginated_metadata(
        self,
        *,
        vector_db_config: object,
        conditions: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        include_chunk_level: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        tag_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataListPaginatedMetadataResponse:
        """
        Get paginated filtered metadata based on conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/list_paginated",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "limit": limit,
                    "offset": offset,
                    "tag_names": tag_names,
                },
                metadata_list_paginated_metadata_params.MetadataListPaginatedMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListPaginatedMetadataResponse,
        )

    def upsert(
        self,
        *,
        metadata: Dict[str, Dict[str, metadata_upsert_params.MetadataMetadataItem]],
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataUpsertResponse:
        """
        Upsert metadata for a given tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/upsert",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "dataslice_id": dataslice_id,
                    "vector_db_config": vector_db_config,
                },
                metadata_upsert_params.MetadataUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataUpsertResponse,
        )


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def file(self) -> AsyncFileResource:
        return AsyncFileResource(self._client)

    @cached_property
    def chunk(self) -> AsyncChunkResource:
        return AsyncChunkResource(self._client)

    @cached_property
    def standardize(self) -> AsyncStandardizeResource:
        return AsyncStandardizeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
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

    async def list_metadata(
        self,
        *,
        vector_db_config: object,
        conditions: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        include_chunk_level: Optional[bool] | NotGiven = NOT_GIVEN,
        tag_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataListMetadataResponse:
        """
        Get paginated filtered metadata based on conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/list",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "tag_names": tag_names,
                },
                metadata_list_metadata_params.MetadataListMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListMetadataResponse,
        )

    async def list_paginated_metadata(
        self,
        *,
        vector_db_config: object,
        conditions: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        include_chunk_level: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        tag_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataListPaginatedMetadataResponse:
        """
        Get paginated filtered metadata based on conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/list_paginated",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "limit": limit,
                    "offset": offset,
                    "tag_names": tag_names,
                },
                metadata_list_paginated_metadata_params.MetadataListPaginatedMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListPaginatedMetadataResponse,
        )

    async def upsert(
        self,
        *,
        metadata: Dict[str, Dict[str, metadata_upsert_params.MetadataMetadataItem]],
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataUpsertResponse:
        """
        Upsert metadata for a given tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/upsert",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "dataslice_id": dataslice_id,
                    "vector_db_config": vector_db_config,
                },
                metadata_upsert_params.MetadataUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataUpsertResponse,
        )


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.delete = to_raw_response_wrapper(
            metadata.delete,
        )
        self.list_metadata = to_raw_response_wrapper(
            metadata.list_metadata,
        )
        self.list_paginated_metadata = to_raw_response_wrapper(
            metadata.list_paginated_metadata,
        )
        self.upsert = to_raw_response_wrapper(
            metadata.upsert,
        )

    @cached_property
    def file(self) -> FileResourceWithRawResponse:
        return FileResourceWithRawResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> ChunkResourceWithRawResponse:
        return ChunkResourceWithRawResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> StandardizeResourceWithRawResponse:
        return StandardizeResourceWithRawResponse(self._metadata.standardize)


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.delete = async_to_raw_response_wrapper(
            metadata.delete,
        )
        self.list_metadata = async_to_raw_response_wrapper(
            metadata.list_metadata,
        )
        self.list_paginated_metadata = async_to_raw_response_wrapper(
            metadata.list_paginated_metadata,
        )
        self.upsert = async_to_raw_response_wrapper(
            metadata.upsert,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithRawResponse:
        return AsyncFileResourceWithRawResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> AsyncChunkResourceWithRawResponse:
        return AsyncChunkResourceWithRawResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> AsyncStandardizeResourceWithRawResponse:
        return AsyncStandardizeResourceWithRawResponse(self._metadata.standardize)


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.delete = to_streamed_response_wrapper(
            metadata.delete,
        )
        self.list_metadata = to_streamed_response_wrapper(
            metadata.list_metadata,
        )
        self.list_paginated_metadata = to_streamed_response_wrapper(
            metadata.list_paginated_metadata,
        )
        self.upsert = to_streamed_response_wrapper(
            metadata.upsert,
        )

    @cached_property
    def file(self) -> FileResourceWithStreamingResponse:
        return FileResourceWithStreamingResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> ChunkResourceWithStreamingResponse:
        return ChunkResourceWithStreamingResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> StandardizeResourceWithStreamingResponse:
        return StandardizeResourceWithStreamingResponse(self._metadata.standardize)


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.delete = async_to_streamed_response_wrapper(
            metadata.delete,
        )
        self.list_metadata = async_to_streamed_response_wrapper(
            metadata.list_metadata,
        )
        self.list_paginated_metadata = async_to_streamed_response_wrapper(
            metadata.list_paginated_metadata,
        )
        self.upsert = async_to_streamed_response_wrapper(
            metadata.upsert,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithStreamingResponse:
        return AsyncFileResourceWithStreamingResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> AsyncChunkResourceWithStreamingResponse:
        return AsyncChunkResourceWithStreamingResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> AsyncStandardizeResourceWithStreamingResponse:
        return AsyncStandardizeResourceWithStreamingResponse(self._metadata.standardize)
