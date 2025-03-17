# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .stripe import (
    StripeResource,
    AsyncStripeResource,
    StripeResourceWithRawResponse,
    AsyncStripeResourceWithRawResponse,
    StripeResourceWithStreamingResponse,
    AsyncStripeResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.console.subscription_retrieve_response import SubscriptionRetrieveResponse

__all__ = ["SubscriptionResource", "AsyncSubscriptionResource"]


class SubscriptionResource(SyncAPIResource):
    @cached_property
    def stripe(self) -> StripeResource:
        return StripeResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return SubscriptionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionRetrieveResponse:
        """
        Get Subscription Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._get(
            "/console/subscription",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveResponse,
        )


class AsyncSubscriptionResource(AsyncAPIResource):
    @cached_property
    def stripe(self) -> AsyncStripeResource:
        return AsyncStripeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncSubscriptionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionRetrieveResponse:
        """
        Get Subscription Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._get(
            "/console/subscription",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveResponse,
        )


class SubscriptionResourceWithRawResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = to_raw_response_wrapper(
            subscription.retrieve,
        )

    @cached_property
    def stripe(self) -> StripeResourceWithRawResponse:
        return StripeResourceWithRawResponse(self._subscription.stripe)


class AsyncSubscriptionResourceWithRawResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = async_to_raw_response_wrapper(
            subscription.retrieve,
        )

    @cached_property
    def stripe(self) -> AsyncStripeResourceWithRawResponse:
        return AsyncStripeResourceWithRawResponse(self._subscription.stripe)


class SubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = to_streamed_response_wrapper(
            subscription.retrieve,
        )

    @cached_property
    def stripe(self) -> StripeResourceWithStreamingResponse:
        return StripeResourceWithStreamingResponse(self._subscription.stripe)


class AsyncSubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = async_to_streamed_response_wrapper(
            subscription.retrieve,
        )

    @cached_property
    def stripe(self) -> AsyncStripeResourceWithStreamingResponse:
        return AsyncStripeResourceWithStreamingResponse(self._subscription.stripe)
