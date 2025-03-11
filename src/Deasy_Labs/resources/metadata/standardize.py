# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.metadata import (
    standardize_list_params,
    standardize_insert_params,
    standardize_get_tag_distribution_params,
)
from ...types.metadata.standardize_get_tag_distribution_response import StandardizeGetTagDistributionResponse

__all__ = ["StandardizeResource", "AsyncStandardizeResource"]


class StandardizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StandardizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return StandardizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StandardizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return StandardizeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Retrieve all standardization mappings for a user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/standardize/list",
            body=maybe_transform({"vector_db_config": vector_db_config}, standardize_list_params.StandardizeListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_tag_distribution(
        self,
        *,
        tag_id: str,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StandardizeGetTagDistributionResponse:
        """
        Get distribution of values for a specific tag, sorted by percentage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/standardize/tag_distribution",
            body=maybe_transform(
                {
                    "tag_id": tag_id,
                    "vector_db_config": vector_db_config,
                },
                standardize_get_tag_distribution_params.StandardizeGetTagDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StandardizeGetTagDistributionResponse,
        )

    def insert(
        self,
        *,
        standard_mapping: object,
        tag_id: str,
        tag_name: str,
        vector_db_config: object,
        taxonomy_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Insert or update a standardization mapping for a tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/standardize/insert",
            body=maybe_transform(
                {
                    "standard_mapping": standard_mapping,
                    "tag_id": tag_id,
                    "tag_name": tag_name,
                    "vector_db_config": vector_db_config,
                    "taxonomy_name": taxonomy_name,
                },
                standardize_insert_params.StandardizeInsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncStandardizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStandardizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStandardizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStandardizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncStandardizeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Retrieve all standardization mappings for a user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/standardize/list",
            body=await async_maybe_transform(
                {"vector_db_config": vector_db_config}, standardize_list_params.StandardizeListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_tag_distribution(
        self,
        *,
        tag_id: str,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StandardizeGetTagDistributionResponse:
        """
        Get distribution of values for a specific tag, sorted by percentage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/standardize/tag_distribution",
            body=await async_maybe_transform(
                {
                    "tag_id": tag_id,
                    "vector_db_config": vector_db_config,
                },
                standardize_get_tag_distribution_params.StandardizeGetTagDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StandardizeGetTagDistributionResponse,
        )

    async def insert(
        self,
        *,
        standard_mapping: object,
        tag_id: str,
        tag_name: str,
        vector_db_config: object,
        taxonomy_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Insert or update a standardization mapping for a tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/standardize/insert",
            body=await async_maybe_transform(
                {
                    "standard_mapping": standard_mapping,
                    "tag_id": tag_id,
                    "tag_name": tag_name,
                    "vector_db_config": vector_db_config,
                    "taxonomy_name": taxonomy_name,
                },
                standardize_insert_params.StandardizeInsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class StandardizeResourceWithRawResponse:
    def __init__(self, standardize: StandardizeResource) -> None:
        self._standardize = standardize

        self.list = to_raw_response_wrapper(
            standardize.list,
        )
        self.get_tag_distribution = to_raw_response_wrapper(
            standardize.get_tag_distribution,
        )
        self.insert = to_raw_response_wrapper(
            standardize.insert,
        )


class AsyncStandardizeResourceWithRawResponse:
    def __init__(self, standardize: AsyncStandardizeResource) -> None:
        self._standardize = standardize

        self.list = async_to_raw_response_wrapper(
            standardize.list,
        )
        self.get_tag_distribution = async_to_raw_response_wrapper(
            standardize.get_tag_distribution,
        )
        self.insert = async_to_raw_response_wrapper(
            standardize.insert,
        )


class StandardizeResourceWithStreamingResponse:
    def __init__(self, standardize: StandardizeResource) -> None:
        self._standardize = standardize

        self.list = to_streamed_response_wrapper(
            standardize.list,
        )
        self.get_tag_distribution = to_streamed_response_wrapper(
            standardize.get_tag_distribution,
        )
        self.insert = to_streamed_response_wrapper(
            standardize.insert,
        )


class AsyncStandardizeResourceWithStreamingResponse:
    def __init__(self, standardize: AsyncStandardizeResource) -> None:
        self._standardize = standardize

        self.list = async_to_streamed_response_wrapper(
            standardize.list,
        )
        self.get_tag_distribution = async_to_streamed_response_wrapper(
            standardize.get_tag_distribution,
        )
        self.insert = async_to_streamed_response_wrapper(
            standardize.insert,
        )
