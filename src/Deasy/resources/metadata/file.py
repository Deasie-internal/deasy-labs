# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ...types.metadata import file_list_params
from ...types.metadata.file_list_response import FileListResponse

__all__ = ["FileResource", "AsyncFileResource"]


class FileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return FileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return FileResourceWithStreamingResponse(self)

    def list(
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
    ) -> FileListResponse:
        """
        Get file level metadata for specified files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/file/list",
            body=maybe_transform(
                {
                    "file_names": file_names,
                    "vector_db_config": vector_db_config,
                },
                file_list_params.FileListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileListResponse,
        )


class AsyncFileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncFileResourceWithStreamingResponse(self)

    async def list(
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
    ) -> FileListResponse:
        """
        Get file level metadata for specified files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/file/list",
            body=await async_maybe_transform(
                {
                    "file_names": file_names,
                    "vector_db_config": vector_db_config,
                },
                file_list_params.FileListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileListResponse,
        )


class FileResourceWithRawResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.list = to_raw_response_wrapper(
            file.list,
        )


class AsyncFileResourceWithRawResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.list = async_to_raw_response_wrapper(
            file.list,
        )


class FileResourceWithStreamingResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.list = to_streamed_response_wrapper(
            file.list,
        )


class AsyncFileResourceWithStreamingResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.list = async_to_streamed_response_wrapper(
            file.list,
        )
