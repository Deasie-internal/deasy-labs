# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .secret import (
    SecretResource,
    AsyncSecretResource,
    SecretResourceWithRawResponse,
    AsyncSecretResourceWithRawResponse,
    SecretResourceWithStreamingResponse,
    AsyncSecretResourceWithStreamingResponse,
)
from .webhook import (
    WebhookResource,
    AsyncWebhookResource,
    WebhookResourceWithRawResponse,
    AsyncWebhookResourceWithRawResponse,
    WebhookResourceWithStreamingResponse,
    AsyncWebhookResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .vector_db import (
    VectorDBResource,
    AsyncVectorDBResource,
    VectorDBResourceWithRawResponse,
    AsyncVectorDBResourceWithRawResponse,
    VectorDBResourceWithStreamingResponse,
    AsyncVectorDBResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .marketplace import (
    MarketplaceResource,
    AsyncMarketplaceResource,
    MarketplaceResourceWithRawResponse,
    AsyncMarketplaceResourceWithRawResponse,
    MarketplaceResourceWithStreamingResponse,
    AsyncMarketplaceResourceWithStreamingResponse,
)
from .llm_provider import (
    LlmProviderResource,
    AsyncLlmProviderResource,
    LlmProviderResourceWithRawResponse,
    AsyncLlmProviderResourceWithRawResponse,
    LlmProviderResourceWithStreamingResponse,
    AsyncLlmProviderResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .subscription.subscription import (
    SubscriptionResource,
    AsyncSubscriptionResource,
    SubscriptionResourceWithRawResponse,
    AsyncSubscriptionResourceWithRawResponse,
    SubscriptionResourceWithStreamingResponse,
    AsyncSubscriptionResourceWithStreamingResponse,
)
from ...types.console_fetch_tiers_response import ConsoleFetchTiersResponse

__all__ = ["ConsoleResource", "AsyncConsoleResource"]


class ConsoleResource(SyncAPIResource):
    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def subscription(self) -> SubscriptionResource:
        return SubscriptionResource(self._client)

    @cached_property
    def marketplace(self) -> MarketplaceResource:
        return MarketplaceResource(self._client)

    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def secret(self) -> SecretResource:
        return SecretResource(self._client)

    @cached_property
    def llm_provider(self) -> LlmProviderResource:
        return LlmProviderResource(self._client)

    @cached_property
    def vector_db(self) -> VectorDBResource:
        return VectorDBResource(self._client)

    @cached_property
    def webhook(self) -> WebhookResource:
        return WebhookResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return ConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return ConsoleResourceWithStreamingResponse(self)

    def fetch_tiers(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConsoleFetchTiersResponse:
        """
        Fetch all available subscription tiers and their limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._get(
            "/console/fetch_tiers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsoleFetchTiersResponse,
        )


class AsyncConsoleResource(AsyncAPIResource):
    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        return AsyncSubscriptionResource(self._client)

    @cached_property
    def marketplace(self) -> AsyncMarketplaceResource:
        return AsyncMarketplaceResource(self._client)

    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def secret(self) -> AsyncSecretResource:
        return AsyncSecretResource(self._client)

    @cached_property
    def llm_provider(self) -> AsyncLlmProviderResource:
        return AsyncLlmProviderResource(self._client)

    @cached_property
    def vector_db(self) -> AsyncVectorDBResource:
        return AsyncVectorDBResource(self._client)

    @cached_property
    def webhook(self) -> AsyncWebhookResource:
        return AsyncWebhookResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncConsoleResourceWithStreamingResponse(self)

    async def fetch_tiers(
        self,
        *,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConsoleFetchTiersResponse:
        """
        Fetch all available subscription tiers and their limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._get(
            "/console/fetch_tiers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsoleFetchTiersResponse,
        )


class ConsoleResourceWithRawResponse:
    def __init__(self, console: ConsoleResource) -> None:
        self._console = console

        self.fetch_tiers = to_raw_response_wrapper(
            console.fetch_tiers,
        )

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._console.token)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithRawResponse:
        return SubscriptionResourceWithRawResponse(self._console.subscription)

    @cached_property
    def marketplace(self) -> MarketplaceResourceWithRawResponse:
        return MarketplaceResourceWithRawResponse(self._console.marketplace)

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._console.user)

    @cached_property
    def secret(self) -> SecretResourceWithRawResponse:
        return SecretResourceWithRawResponse(self._console.secret)

    @cached_property
    def llm_provider(self) -> LlmProviderResourceWithRawResponse:
        return LlmProviderResourceWithRawResponse(self._console.llm_provider)

    @cached_property
    def vector_db(self) -> VectorDBResourceWithRawResponse:
        return VectorDBResourceWithRawResponse(self._console.vector_db)

    @cached_property
    def webhook(self) -> WebhookResourceWithRawResponse:
        return WebhookResourceWithRawResponse(self._console.webhook)


class AsyncConsoleResourceWithRawResponse:
    def __init__(self, console: AsyncConsoleResource) -> None:
        self._console = console

        self.fetch_tiers = async_to_raw_response_wrapper(
            console.fetch_tiers,
        )

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._console.token)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithRawResponse:
        return AsyncSubscriptionResourceWithRawResponse(self._console.subscription)

    @cached_property
    def marketplace(self) -> AsyncMarketplaceResourceWithRawResponse:
        return AsyncMarketplaceResourceWithRawResponse(self._console.marketplace)

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._console.user)

    @cached_property
    def secret(self) -> AsyncSecretResourceWithRawResponse:
        return AsyncSecretResourceWithRawResponse(self._console.secret)

    @cached_property
    def llm_provider(self) -> AsyncLlmProviderResourceWithRawResponse:
        return AsyncLlmProviderResourceWithRawResponse(self._console.llm_provider)

    @cached_property
    def vector_db(self) -> AsyncVectorDBResourceWithRawResponse:
        return AsyncVectorDBResourceWithRawResponse(self._console.vector_db)

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithRawResponse:
        return AsyncWebhookResourceWithRawResponse(self._console.webhook)


class ConsoleResourceWithStreamingResponse:
    def __init__(self, console: ConsoleResource) -> None:
        self._console = console

        self.fetch_tiers = to_streamed_response_wrapper(
            console.fetch_tiers,
        )

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._console.token)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithStreamingResponse:
        return SubscriptionResourceWithStreamingResponse(self._console.subscription)

    @cached_property
    def marketplace(self) -> MarketplaceResourceWithStreamingResponse:
        return MarketplaceResourceWithStreamingResponse(self._console.marketplace)

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._console.user)

    @cached_property
    def secret(self) -> SecretResourceWithStreamingResponse:
        return SecretResourceWithStreamingResponse(self._console.secret)

    @cached_property
    def llm_provider(self) -> LlmProviderResourceWithStreamingResponse:
        return LlmProviderResourceWithStreamingResponse(self._console.llm_provider)

    @cached_property
    def vector_db(self) -> VectorDBResourceWithStreamingResponse:
        return VectorDBResourceWithStreamingResponse(self._console.vector_db)

    @cached_property
    def webhook(self) -> WebhookResourceWithStreamingResponse:
        return WebhookResourceWithStreamingResponse(self._console.webhook)


class AsyncConsoleResourceWithStreamingResponse:
    def __init__(self, console: AsyncConsoleResource) -> None:
        self._console = console

        self.fetch_tiers = async_to_streamed_response_wrapper(
            console.fetch_tiers,
        )

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._console.token)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        return AsyncSubscriptionResourceWithStreamingResponse(self._console.subscription)

    @cached_property
    def marketplace(self) -> AsyncMarketplaceResourceWithStreamingResponse:
        return AsyncMarketplaceResourceWithStreamingResponse(self._console.marketplace)

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._console.user)

    @cached_property
    def secret(self) -> AsyncSecretResourceWithStreamingResponse:
        return AsyncSecretResourceWithStreamingResponse(self._console.secret)

    @cached_property
    def llm_provider(self) -> AsyncLlmProviderResourceWithStreamingResponse:
        return AsyncLlmProviderResourceWithStreamingResponse(self._console.llm_provider)

    @cached_property
    def vector_db(self) -> AsyncVectorDBResourceWithStreamingResponse:
        return AsyncVectorDBResourceWithStreamingResponse(self._console.vector_db)

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithStreamingResponse:
        return AsyncWebhookResourceWithStreamingResponse(self._console.webhook)
