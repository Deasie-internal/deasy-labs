# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["WebhookResource", "AsyncWebhookResource"]


class WebhookResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return WebhookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return WebhookResourceWithStreamingResponse(self)

    def handle_stripe(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Handle Stripe webhook events."""
        return self._post(
            "/console/webhook/stripe",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncWebhookResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncWebhookResourceWithStreamingResponse(self)

    async def handle_stripe(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Handle Stripe webhook events."""
        return await self._post(
            "/console/webhook/stripe",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class WebhookResourceWithRawResponse:
    def __init__(self, webhook: WebhookResource) -> None:
        self._webhook = webhook

        self.handle_stripe = to_raw_response_wrapper(
            webhook.handle_stripe,
        )


class AsyncWebhookResourceWithRawResponse:
    def __init__(self, webhook: AsyncWebhookResource) -> None:
        self._webhook = webhook

        self.handle_stripe = async_to_raw_response_wrapper(
            webhook.handle_stripe,
        )


class WebhookResourceWithStreamingResponse:
    def __init__(self, webhook: WebhookResource) -> None:
        self._webhook = webhook

        self.handle_stripe = to_streamed_response_wrapper(
            webhook.handle_stripe,
        )


class AsyncWebhookResourceWithStreamingResponse:
    def __init__(self, webhook: AsyncWebhookResource) -> None:
        self._webhook = webhook

        self.handle_stripe = async_to_streamed_response_wrapper(
            webhook.handle_stripe,
        )
