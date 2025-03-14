# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import generate_file_tag_create_params
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
from ..types.generate_file_tag_create_response import GenerateFileTagCreateResponse

__all__ = ["GenerateFileTagsResource", "AsyncGenerateFileTagsResource"]


class GenerateFileTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateFileTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return GenerateFileTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateFileTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return GenerateFileTagsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        endpoint_manager_config: object,
        file_names: List[str],
        tags: Optional[Dict[str, object]],
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateFileTagCreateResponse:
        """
        Generate file level metadata for specified files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generate_file_tags",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "file_names": file_names,
                    "tags": tags,
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "job_id": job_id,
                },
                generate_file_tag_create_params.GenerateFileTagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateFileTagCreateResponse,
        )


class AsyncGenerateFileTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateFileTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateFileTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateFileTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncGenerateFileTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        endpoint_manager_config: object,
        file_names: List[str],
        tags: Optional[Dict[str, object]],
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GenerateFileTagCreateResponse:
        """
        Generate file level metadata for specified files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generate_file_tags",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "file_names": file_names,
                    "tags": tags,
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "job_id": job_id,
                },
                generate_file_tag_create_params.GenerateFileTagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateFileTagCreateResponse,
        )


class GenerateFileTagsResourceWithRawResponse:
    def __init__(self, generate_file_tags: GenerateFileTagsResource) -> None:
        self._generate_file_tags = generate_file_tags

        self.create = to_raw_response_wrapper(
            generate_file_tags.create,
        )


class AsyncGenerateFileTagsResourceWithRawResponse:
    def __init__(self, generate_file_tags: AsyncGenerateFileTagsResource) -> None:
        self._generate_file_tags = generate_file_tags

        self.create = async_to_raw_response_wrapper(
            generate_file_tags.create,
        )


class GenerateFileTagsResourceWithStreamingResponse:
    def __init__(self, generate_file_tags: GenerateFileTagsResource) -> None:
        self._generate_file_tags = generate_file_tags

        self.create = to_streamed_response_wrapper(
            generate_file_tags.create,
        )


class AsyncGenerateFileTagsResourceWithStreamingResponse:
    def __init__(self, generate_file_tags: AsyncGenerateFileTagsResource) -> None:
        self._generate_file_tags = generate_file_tags

        self.create = async_to_streamed_response_wrapper(
            generate_file_tags.create,
        )
