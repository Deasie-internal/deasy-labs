# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import contextualize_create_params
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
from ..types.contextualize_create_response import ContextualizeCreateResponse

__all__ = ["ContextualizeResource", "AsyncContextualizeResource"]


class ContextualizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextualizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return ContextualizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextualizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return ContextualizeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        endpoint_manager_config: object,
        vector_db_config: object,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ignore_untagged_files: bool | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        verbose: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextualizeCreateResponse:
        """
        Contextualize each chunk within the respective document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contextualize",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                    "ignore_untagged_files": ignore_untagged_files,
                    "job_id": job_id,
                    "overwrite": overwrite,
                    "usecase_id": usecase_id,
                    "verbose": verbose,
                },
                contextualize_create_params.ContextualizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextualizeCreateResponse,
        )


class AsyncContextualizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextualizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContextualizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextualizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncContextualizeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        endpoint_manager_config: object,
        vector_db_config: object,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        ignore_untagged_files: bool | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        verbose: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextualizeCreateResponse:
        """
        Contextualize each chunk within the respective document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contextualize",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                    "ignore_untagged_files": ignore_untagged_files,
                    "job_id": job_id,
                    "overwrite": overwrite,
                    "usecase_id": usecase_id,
                    "verbose": verbose,
                },
                contextualize_create_params.ContextualizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextualizeCreateResponse,
        )


class ContextualizeResourceWithRawResponse:
    def __init__(self, contextualize: ContextualizeResource) -> None:
        self._contextualize = contextualize

        self.create = to_raw_response_wrapper(
            contextualize.create,
        )


class AsyncContextualizeResourceWithRawResponse:
    def __init__(self, contextualize: AsyncContextualizeResource) -> None:
        self._contextualize = contextualize

        self.create = async_to_raw_response_wrapper(
            contextualize.create,
        )


class ContextualizeResourceWithStreamingResponse:
    def __init__(self, contextualize: ContextualizeResource) -> None:
        self._contextualize = contextualize

        self.create = to_streamed_response_wrapper(
            contextualize.create,
        )


class AsyncContextualizeResourceWithStreamingResponse:
    def __init__(self, contextualize: AsyncContextualizeResource) -> None:
        self._contextualize = contextualize

        self.create = async_to_streamed_response_wrapper(
            contextualize.create,
        )
