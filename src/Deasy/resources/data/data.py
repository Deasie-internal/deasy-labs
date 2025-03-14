# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

import httpx

from ...types import (
    data_list_paginated_params,
    data_get_document_text_params,
    data_get_vdb_total_files_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
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
from ...types.data_list_paginated_response import DataListPaginatedResponse
from ...types.data_get_document_text_response import DataGetDocumentTextResponse
from ...types.data_get_vdb_total_files_response import DataGetVdbTotalFilesResponse

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)

    def get_document_text(
        self,
        *,
        file_names: List[str],
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGetDocumentTextResponse:
        """
        Retrieve the raw text content for specified documents from the vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/document_text",
            body=maybe_transform(
                {
                    "file_names": file_names,
                    "vector_db_config": vector_db_config,
                },
                data_get_document_text_params.DataGetDocumentTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGetDocumentTextResponse,
        )

    def get_vdb_total_files(
        self,
        *,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGetVdbTotalFilesResponse:
        """Get the total number of files in the vector database.

        Returns cached value if
        available, while triggering a background refresh.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data/file_count",
            body=maybe_transform(
                {"vector_db_config": vector_db_config}, data_get_vdb_total_files_params.DataGetVdbTotalFilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGetVdbTotalFilesResponse,
        )

    def list_paginated(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        entities_already_scrolled: Optional[List[str]] | NotGiven = NOT_GIVEN,
        group_by: str | NotGiven = NOT_GIVEN,
        hard_limit: Optional[int] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: Union[int, str] | NotGiven = NOT_GIVEN,
        scroll_limit: Optional[int] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataListPaginatedResponse:
        """
        Retrieve a paginated list of files/nodes from the vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/data/list_paginated",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "entities_already_scrolled": entities_already_scrolled,
                    "group_by": group_by,
                    "hard_limit": hard_limit,
                    "limit": limit,
                    "offset": offset,
                    "scroll_limit": scroll_limit,
                    "search_query": search_query,
                },
                data_list_paginated_params.DataListPaginatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataListPaginatedResponse,
        )


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)

    async def get_document_text(
        self,
        *,
        file_names: List[str],
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGetDocumentTextResponse:
        """
        Retrieve the raw text content for specified documents from the vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/document_text",
            body=await async_maybe_transform(
                {
                    "file_names": file_names,
                    "vector_db_config": vector_db_config,
                },
                data_get_document_text_params.DataGetDocumentTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGetDocumentTextResponse,
        )

    async def get_vdb_total_files(
        self,
        *,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataGetVdbTotalFilesResponse:
        """Get the total number of files in the vector database.

        Returns cached value if
        available, while triggering a background refresh.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data/file_count",
            body=await async_maybe_transform(
                {"vector_db_config": vector_db_config}, data_get_vdb_total_files_params.DataGetVdbTotalFilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataGetVdbTotalFilesResponse,
        )

    async def list_paginated(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        entities_already_scrolled: Optional[List[str]] | NotGiven = NOT_GIVEN,
        group_by: str | NotGiven = NOT_GIVEN,
        hard_limit: Optional[int] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: Union[int, str] | NotGiven = NOT_GIVEN,
        scroll_limit: Optional[int] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataListPaginatedResponse:
        """
        Retrieve a paginated list of files/nodes from the vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/data/list_paginated",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "entities_already_scrolled": entities_already_scrolled,
                    "group_by": group_by,
                    "hard_limit": hard_limit,
                    "limit": limit,
                    "offset": offset,
                    "scroll_limit": scroll_limit,
                    "search_query": search_query,
                },
                data_list_paginated_params.DataListPaginatedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataListPaginatedResponse,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.get_document_text = to_raw_response_wrapper(
            data.get_document_text,
        )
        self.get_vdb_total_files = to_raw_response_wrapper(
            data.get_vdb_total_files,
        )
        self.list_paginated = to_raw_response_wrapper(
            data.list_paginated,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._data.metadata)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.get_document_text = async_to_raw_response_wrapper(
            data.get_document_text,
        )
        self.get_vdb_total_files = async_to_raw_response_wrapper(
            data.get_vdb_total_files,
        )
        self.list_paginated = async_to_raw_response_wrapper(
            data.list_paginated,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._data.metadata)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.get_document_text = to_streamed_response_wrapper(
            data.get_document_text,
        )
        self.get_vdb_total_files = to_streamed_response_wrapper(
            data.get_vdb_total_files,
        )
        self.list_paginated = to_streamed_response_wrapper(
            data.list_paginated,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._data.metadata)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.get_document_text = async_to_streamed_response_wrapper(
            data.get_document_text,
        )
        self.get_vdb_total_files = async_to_streamed_response_wrapper(
            data.get_vdb_total_files,
        )
        self.list_paginated = async_to_streamed_response_wrapper(
            data.list_paginated,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._data.metadata)
