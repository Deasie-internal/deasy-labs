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
from ...types.console import vector_db_validate_params, vector_db_check_indexes_params
from ...types.console.vector_db_validate_response import VectorDBValidateResponse
from ...types.console.vector_db_check_indexes_response import VectorDBCheckIndexesResponse

__all__ = ["VectorDBResource", "AsyncVectorDBResource"]


class VectorDBResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorDBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return VectorDBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorDBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return VectorDBResourceWithStreamingResponse(self)

    def check_indexes(
        self,
        *,
        body: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBCheckIndexesResponse:
        """
        Check if the indexes exist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/vector-db/check-index-fields",
            body=maybe_transform(body, vector_db_check_indexes_params.VectorDBCheckIndexesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBCheckIndexesResponse,
        )

    def validate(
        self,
        *,
        body: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBValidateResponse:
        """
        Console endpoint for validating vector database configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/console/vector-db/validate",
            body=maybe_transform(body, vector_db_validate_params.VectorDBValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBValidateResponse,
        )


class AsyncVectorDBResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorDBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorDBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorDBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncVectorDBResourceWithStreamingResponse(self)

    async def check_indexes(
        self,
        *,
        body: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBCheckIndexesResponse:
        """
        Check if the indexes exist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/vector-db/check-index-fields",
            body=await async_maybe_transform(body, vector_db_check_indexes_params.VectorDBCheckIndexesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBCheckIndexesResponse,
        )

    async def validate(
        self,
        *,
        body: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorDBValidateResponse:
        """
        Console endpoint for validating vector database configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/console/vector-db/validate",
            body=await async_maybe_transform(body, vector_db_validate_params.VectorDBValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorDBValidateResponse,
        )


class VectorDBResourceWithRawResponse:
    def __init__(self, vector_db: VectorDBResource) -> None:
        self._vector_db = vector_db

        self.check_indexes = to_raw_response_wrapper(
            vector_db.check_indexes,
        )
        self.validate = to_raw_response_wrapper(
            vector_db.validate,
        )


class AsyncVectorDBResourceWithRawResponse:
    def __init__(self, vector_db: AsyncVectorDBResource) -> None:
        self._vector_db = vector_db

        self.check_indexes = async_to_raw_response_wrapper(
            vector_db.check_indexes,
        )
        self.validate = async_to_raw_response_wrapper(
            vector_db.validate,
        )


class VectorDBResourceWithStreamingResponse:
    def __init__(self, vector_db: VectorDBResource) -> None:
        self._vector_db = vector_db

        self.check_indexes = to_streamed_response_wrapper(
            vector_db.check_indexes,
        )
        self.validate = to_streamed_response_wrapper(
            vector_db.validate,
        )


class AsyncVectorDBResourceWithStreamingResponse:
    def __init__(self, vector_db: AsyncVectorDBResource) -> None:
        self._vector_db = vector_db

        self.check_indexes = async_to_streamed_response_wrapper(
            vector_db.check_indexes,
        )
        self.validate = async_to_streamed_response_wrapper(
            vector_db.validate,
        )
