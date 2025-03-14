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
from ...types.console import secret_get_params, secret_store_params
from ...types.console.secret_get_response import SecretGetResponse
from ...types.console.secret_store_response import SecretStoreResponse

__all__ = ["SecretResource", "AsyncSecretResource"]


class SecretResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return SecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return SecretResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        secret_name: str,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetResponse:
        """
        Get a secret from GCP Secret Manager.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/secret/get",
            body=maybe_transform({"secret_name": secret_name}, secret_get_params.SecretGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretGetResponse,
        )

    def store(
        self,
        *,
        secret_name: str,
        secret_value: str,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretStoreResponse:
        """
        Store a secret in GCP Secret Manager.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/secret/store",
            body=maybe_transform(
                {
                    "secret_name": secret_name,
                    "secret_value": secret_value,
                },
                secret_store_params.SecretStoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretStoreResponse,
        )


class AsyncSecretResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncSecretResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        secret_name: str,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetResponse:
        """
        Get a secret from GCP Secret Manager.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/secret/get",
            body=await async_maybe_transform({"secret_name": secret_name}, secret_get_params.SecretGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretGetResponse,
        )

    async def store(
        self,
        *,
        secret_name: str,
        secret_value: str,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretStoreResponse:
        """
        Store a secret in GCP Secret Manager.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/secret/store",
            body=await async_maybe_transform(
                {
                    "secret_name": secret_name,
                    "secret_value": secret_value,
                },
                secret_store_params.SecretStoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretStoreResponse,
        )


class SecretResourceWithRawResponse:
    def __init__(self, secret: SecretResource) -> None:
        self._secret = secret

        self.get = to_raw_response_wrapper(
            secret.get,
        )
        self.store = to_raw_response_wrapper(
            secret.store,
        )


class AsyncSecretResourceWithRawResponse:
    def __init__(self, secret: AsyncSecretResource) -> None:
        self._secret = secret

        self.get = async_to_raw_response_wrapper(
            secret.get,
        )
        self.store = async_to_raw_response_wrapper(
            secret.store,
        )


class SecretResourceWithStreamingResponse:
    def __init__(self, secret: SecretResource) -> None:
        self._secret = secret

        self.get = to_streamed_response_wrapper(
            secret.get,
        )
        self.store = to_streamed_response_wrapper(
            secret.store,
        )


class AsyncSecretResourceWithStreamingResponse:
    def __init__(self, secret: AsyncSecretResource) -> None:
        self._secret = secret

        self.get = async_to_streamed_response_wrapper(
            secret.get,
        )
        self.store = async_to_streamed_response_wrapper(
            secret.store,
        )
