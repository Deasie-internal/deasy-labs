# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    metadata_list_params,
    metadata_delete_params,
    metadata_upsert_params,
    metadata_list_paginated_params,
    metadata_get_distributions_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.condition_input_param import ConditionInputParam
from ..types.metadata_list_response import MetadataListResponse
from ..types.metadata_delete_response import MetadataDeleteResponse
from ..types.metadata_upsert_response import MetadataUpsertResponse
from ..types.metadata_list_paginated_response import MetadataListPaginatedResponse
from ..types.metadata_get_distributions_response import MetadataGetDistributionsResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        vdb_profile_name: str,
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
    ) -> MetadataListResponse:
        """
        Get paginated filtered metadata based on conditions

        Attributes:

            vdb_profile_name: The name of the vdb profile to include in the dataslice.
            dataslice_id: The dataslice for getting files from.
            conditions: The conditions to filter the files by.
            tag_names: The names of the tags to include in the metadata.
            include_chunk_level: Whether to include the chunk-level metadata.

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
                    "vdb_profile_name": vdb_profile_name,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "tag_names": tag_names,
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
        vdb_profile_name: str,
        conditions: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
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
        Delete metadata for specified files and tags

        Attributes: vector_db_config: The vector database configuration to use.
        file_names: The files to delete the metadata for. tags: The tags to delete the
        metadata for. conditions: The conditions to delete the metadata for.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/delete",
            body=maybe_transform(
                {
                    "vdb_profile_name": vdb_profile_name,
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

    def get_distributions(
        self,
        *,
        vdb_profile_name: str,
        analysis_level: Literal["file", "chunk", "both"] | NotGiven = NOT_GIVEN,
        schema_name: Optional[str] | NotGiven = NOT_GIVEN,
        tag_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetDistributionsResponse:
        """
        Get distribution of values for a specific tag, sorted by percentage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/get_distributions",
            body=maybe_transform(
                {
                    "vdb_profile_name": vdb_profile_name,
                    "analysis_level": analysis_level,
                    "schema_name": schema_name,
                    "tag_names": tag_names,
                },
                metadata_get_distributions_params.MetadataGetDistributionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetDistributionsResponse,
        )

    def list_paginated(
        self,
        *,
        vdb_profile_name: str,
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
    ) -> MetadataListPaginatedResponse:
        """
        Get paginated filtered metadata based on conditions

        Attributes:

            vdb_profile_name: The name of the vdb profile to include in the dataslice.
            dataslice_id: The dataslice for getting files from.
            conditions: The conditions to filter the files by.
            tag_names: The names of the tags to include in the metadata.
            include_chunk_level: Whether to include the chunk-level metadata.
            offset: The offset to start the pagination from.
            limit: The limit to the number of metadata to return.

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
                    "vdb_profile_name": vdb_profile_name,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "limit": limit,
                    "offset": offset,
                    "tag_names": tag_names,
                },
                metadata_list_paginated_params.MetadataListPaginatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListPaginatedResponse,
        )

    def upsert(
        self,
        *,
        metadata: Dict[str, Dict[str, metadata_upsert_params.MetadataMetadataItem]],
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        vdb_profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataUpsertResponse:
        """
        Upsert metadata for files and tags

        Attributes:

            vdb_profile_name: The name of the vdb profile to include in the dataslice.
            dataslice_id: The dataslice for getting files from.
            metadata: The metadata to upsert with the form {file_name: {tag_name: tag_value}}.

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
                    "vdb_profile_name": vdb_profile_name,
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
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        vdb_profile_name: str,
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
    ) -> MetadataListResponse:
        """
        Get paginated filtered metadata based on conditions

        Attributes:

            vdb_profile_name: The name of the vdb profile to include in the dataslice.
            dataslice_id: The dataslice for getting files from.
            conditions: The conditions to filter the files by.
            tag_names: The names of the tags to include in the metadata.
            include_chunk_level: Whether to include the chunk-level metadata.

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
                    "vdb_profile_name": vdb_profile_name,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "tag_names": tag_names,
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
        vdb_profile_name: str,
        conditions: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
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
        Delete metadata for specified files and tags

        Attributes: vector_db_config: The vector database configuration to use.
        file_names: The files to delete the metadata for. tags: The tags to delete the
        metadata for. conditions: The conditions to delete the metadata for.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/delete",
            body=await async_maybe_transform(
                {
                    "vdb_profile_name": vdb_profile_name,
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

    async def get_distributions(
        self,
        *,
        vdb_profile_name: str,
        analysis_level: Literal["file", "chunk", "both"] | NotGiven = NOT_GIVEN,
        schema_name: Optional[str] | NotGiven = NOT_GIVEN,
        tag_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetDistributionsResponse:
        """
        Get distribution of values for a specific tag, sorted by percentage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/get_distributions",
            body=await async_maybe_transform(
                {
                    "vdb_profile_name": vdb_profile_name,
                    "analysis_level": analysis_level,
                    "schema_name": schema_name,
                    "tag_names": tag_names,
                },
                metadata_get_distributions_params.MetadataGetDistributionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetDistributionsResponse,
        )

    async def list_paginated(
        self,
        *,
        vdb_profile_name: str,
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
    ) -> MetadataListPaginatedResponse:
        """
        Get paginated filtered metadata based on conditions

        Attributes:

            vdb_profile_name: The name of the vdb profile to include in the dataslice.
            dataslice_id: The dataslice for getting files from.
            conditions: The conditions to filter the files by.
            tag_names: The names of the tags to include in the metadata.
            include_chunk_level: Whether to include the chunk-level metadata.
            offset: The offset to start the pagination from.
            limit: The limit to the number of metadata to return.

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
                    "vdb_profile_name": vdb_profile_name,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "include_chunk_level": include_chunk_level,
                    "limit": limit,
                    "offset": offset,
                    "tag_names": tag_names,
                },
                metadata_list_paginated_params.MetadataListPaginatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataListPaginatedResponse,
        )

    async def upsert(
        self,
        *,
        metadata: Dict[str, Dict[str, metadata_upsert_params.MetadataMetadataItem]],
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        vdb_profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataUpsertResponse:
        """
        Upsert metadata for files and tags

        Attributes:

            vdb_profile_name: The name of the vdb profile to include in the dataslice.
            dataslice_id: The dataslice for getting files from.
            metadata: The metadata to upsert with the form {file_name: {tag_name: tag_value}}.

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
                    "vdb_profile_name": vdb_profile_name,
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

        self.list = to_raw_response_wrapper(
            metadata.list,
        )
        self.delete = to_raw_response_wrapper(
            metadata.delete,
        )
        self.get_distributions = to_raw_response_wrapper(
            metadata.get_distributions,
        )
        self.list_paginated = to_raw_response_wrapper(
            metadata.list_paginated,
        )
        self.upsert = to_raw_response_wrapper(
            metadata.upsert,
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
        self.get_distributions = async_to_raw_response_wrapper(
            metadata.get_distributions,
        )
        self.list_paginated = async_to_raw_response_wrapper(
            metadata.list_paginated,
        )
        self.upsert = async_to_raw_response_wrapper(
            metadata.upsert,
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
        self.get_distributions = to_streamed_response_wrapper(
            metadata.get_distributions,
        )
        self.list_paginated = to_streamed_response_wrapper(
            metadata.list_paginated,
        )
        self.upsert = to_streamed_response_wrapper(
            metadata.upsert,
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
        self.get_distributions = async_to_streamed_response_wrapper(
            metadata.get_distributions,
        )
        self.list_paginated = async_to_streamed_response_wrapper(
            metadata.list_paginated,
        )
        self.upsert = async_to_streamed_response_wrapper(
            metadata.upsert,
        )
