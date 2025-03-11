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
from ...types.console import llm_provider_validate_params
from ...types.console.llm_provider_validate_response import LlmProviderValidateResponse

__all__ = ["LlmProviderResource", "AsyncLlmProviderResource"]


class LlmProviderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return LlmProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return LlmProviderResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        endpoint_manager_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmProviderValidateResponse:
        """
        Validate Llm Provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/llm-provider/validate",
            body=maybe_transform(
                {"endpoint_manager_config": endpoint_manager_config},
                llm_provider_validate_params.LlmProviderValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmProviderValidateResponse,
        )


class AsyncLlmProviderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncLlmProviderResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        endpoint_manager_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmProviderValidateResponse:
        """
        Validate Llm Provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/llm-provider/validate",
            body=await async_maybe_transform(
                {"endpoint_manager_config": endpoint_manager_config},
                llm_provider_validate_params.LlmProviderValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmProviderValidateResponse,
        )


class LlmProviderResourceWithRawResponse:
    def __init__(self, llm_provider: LlmProviderResource) -> None:
        self._llm_provider = llm_provider

        self.validate = to_raw_response_wrapper(
            llm_provider.validate,
        )


class AsyncLlmProviderResourceWithRawResponse:
    def __init__(self, llm_provider: AsyncLlmProviderResource) -> None:
        self._llm_provider = llm_provider

        self.validate = async_to_raw_response_wrapper(
            llm_provider.validate,
        )


class LlmProviderResourceWithStreamingResponse:
    def __init__(self, llm_provider: LlmProviderResource) -> None:
        self._llm_provider = llm_provider

        self.validate = to_streamed_response_wrapper(
            llm_provider.validate,
        )


class AsyncLlmProviderResourceWithStreamingResponse:
    def __init__(self, llm_provider: AsyncLlmProviderResource) -> None:
        self._llm_provider = llm_provider

        self.validate = async_to_streamed_response_wrapper(
            llm_provider.validate,
        )
