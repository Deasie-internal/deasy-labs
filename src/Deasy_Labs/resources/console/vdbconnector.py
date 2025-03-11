# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.console import vdbconnector_delete_params, vdbconnector_get_delete_stats_params
from ...types.console.vdbconnector_delete_response import VdbconnectorDeleteResponse
from ...types.console.vdbconnector_get_delete_stats_response import VdbconnectorGetDeleteStatsResponse

__all__ = ["VdbconnectorResource", "AsyncVdbconnectorResource"]


class VdbconnectorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VdbconnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return VdbconnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VdbconnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return VdbconnectorResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VdbconnectorDeleteResponse:
        """
        Delete a connector

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/vdbconnector/delete",
            body=maybe_transform(
                {"vector_db_config": vector_db_config}, vdbconnector_delete_params.VdbconnectorDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VdbconnectorDeleteResponse,
        )

    def get_delete_stats(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VdbconnectorGetDeleteStatsResponse:
        """
        Get tag delete stats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/vdbconnector/delete_stats",
            body=maybe_transform(
                {"vector_db_config": vector_db_config},
                vdbconnector_get_delete_stats_params.VdbconnectorGetDeleteStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VdbconnectorGetDeleteStatsResponse,
        )


class AsyncVdbconnectorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVdbconnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVdbconnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVdbconnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncVdbconnectorResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VdbconnectorDeleteResponse:
        """
        Delete a connector

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/vdbconnector/delete",
            body=await async_maybe_transform(
                {"vector_db_config": vector_db_config}, vdbconnector_delete_params.VdbconnectorDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VdbconnectorDeleteResponse,
        )

    async def get_delete_stats(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VdbconnectorGetDeleteStatsResponse:
        """
        Get tag delete stats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/vdbconnector/delete_stats",
            body=await async_maybe_transform(
                {"vector_db_config": vector_db_config},
                vdbconnector_get_delete_stats_params.VdbconnectorGetDeleteStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VdbconnectorGetDeleteStatsResponse,
        )


class VdbconnectorResourceWithRawResponse:
    def __init__(self, vdbconnector: VdbconnectorResource) -> None:
        self._vdbconnector = vdbconnector

        self.delete = to_raw_response_wrapper(
            vdbconnector.delete,
        )
        self.get_delete_stats = to_raw_response_wrapper(
            vdbconnector.get_delete_stats,
        )


class AsyncVdbconnectorResourceWithRawResponse:
    def __init__(self, vdbconnector: AsyncVdbconnectorResource) -> None:
        self._vdbconnector = vdbconnector

        self.delete = async_to_raw_response_wrapper(
            vdbconnector.delete,
        )
        self.get_delete_stats = async_to_raw_response_wrapper(
            vdbconnector.get_delete_stats,
        )


class VdbconnectorResourceWithStreamingResponse:
    def __init__(self, vdbconnector: VdbconnectorResource) -> None:
        self._vdbconnector = vdbconnector

        self.delete = to_streamed_response_wrapper(
            vdbconnector.delete,
        )
        self.get_delete_stats = to_streamed_response_wrapper(
            vdbconnector.get_delete_stats,
        )


class AsyncVdbconnectorResourceWithStreamingResponse:
    def __init__(self, vdbconnector: AsyncVdbconnectorResource) -> None:
        self._vdbconnector = vdbconnector

        self.delete = async_to_streamed_response_wrapper(
            vdbconnector.delete,
        )
        self.get_delete_stats = async_to_streamed_response_wrapper(
            vdbconnector.get_delete_stats,
        )
