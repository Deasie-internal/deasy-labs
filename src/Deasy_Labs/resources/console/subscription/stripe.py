# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.console.subscription import stripe_create_session_params
from ....types.console.subscription.stripe_cancel_response import StripeCancelResponse
from ....types.console.subscription.stripe_validate_response import StripeValidateResponse
from ....types.console.subscription.stripe_create_session_response import StripeCreateSessionResponse

__all__ = ["StripeResource", "AsyncStripeResource"]


class StripeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StripeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return StripeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StripeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return StripeResourceWithStreamingResponse(self)

    def cancel(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StripeCancelResponse:
        """
        Cancel a Stripe subscription at the end of the current billing period.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/subscription/stripe/unsubscribe",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StripeCancelResponse,
        )

    def create_session(
        self,
        *,
        tier_id: str,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StripeCreateSessionResponse:
        """
        Create or update Stripe subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/subscription/stripe/payment",
            body=maybe_transform({"tier_id": tier_id}, stripe_create_session_params.StripeCreateSessionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StripeCreateSessionResponse,
        )

    def validate(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StripeValidateResponse:
        """
        Validate the current subscription status and handle period-end cancellations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/subscription/stripe/validate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StripeValidateResponse,
        )


class AsyncStripeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStripeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStripeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStripeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncStripeResourceWithStreamingResponse(self)

    async def cancel(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StripeCancelResponse:
        """
        Cancel a Stripe subscription at the end of the current billing period.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/subscription/stripe/unsubscribe",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StripeCancelResponse,
        )

    async def create_session(
        self,
        *,
        tier_id: str,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StripeCreateSessionResponse:
        """
        Create or update Stripe subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/subscription/stripe/payment",
            body=await async_maybe_transform(
                {"tier_id": tier_id}, stripe_create_session_params.StripeCreateSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StripeCreateSessionResponse,
        )

    async def validate(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StripeValidateResponse:
        """
        Validate the current subscription status and handle period-end cancellations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/subscription/stripe/validate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StripeValidateResponse,
        )


class StripeResourceWithRawResponse:
    def __init__(self, stripe: StripeResource) -> None:
        self._stripe = stripe

        self.cancel = to_raw_response_wrapper(
            stripe.cancel,
        )
        self.create_session = to_raw_response_wrapper(
            stripe.create_session,
        )
        self.validate = to_raw_response_wrapper(
            stripe.validate,
        )


class AsyncStripeResourceWithRawResponse:
    def __init__(self, stripe: AsyncStripeResource) -> None:
        self._stripe = stripe

        self.cancel = async_to_raw_response_wrapper(
            stripe.cancel,
        )
        self.create_session = async_to_raw_response_wrapper(
            stripe.create_session,
        )
        self.validate = async_to_raw_response_wrapper(
            stripe.validate,
        )


class StripeResourceWithStreamingResponse:
    def __init__(self, stripe: StripeResource) -> None:
        self._stripe = stripe

        self.cancel = to_streamed_response_wrapper(
            stripe.cancel,
        )
        self.create_session = to_streamed_response_wrapper(
            stripe.create_session,
        )
        self.validate = to_streamed_response_wrapper(
            stripe.validate,
        )


class AsyncStripeResourceWithStreamingResponse:
    def __init__(self, stripe: AsyncStripeResource) -> None:
        self._stripe = stripe

        self.cancel = async_to_streamed_response_wrapper(
            stripe.cancel,
        )
        self.create_session = async_to_streamed_response_wrapper(
            stripe.create_session,
        )
        self.validate = async_to_streamed_response_wrapper(
            stripe.validate,
        )
