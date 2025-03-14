# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import refine_tag_refine_params
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
from ..types.refine_tag_refine_response import RefineTagRefineResponse

__all__ = ["RefineTagResource", "AsyncRefineTagResource"]


class RefineTagResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefineTagResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return RefineTagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefineTagResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return RefineTagResourceWithStreamingResponse(self)

    def refine(
        self,
        *,
        endpoint_manager_config: object,
        tag_to_refine: Dict[str, refine_tag_refine_params.TagToRefine],
        vector_db_config: object,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RefineTagRefineResponse:
        """
        Refine an existing tag by analyzing its previous extractions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/refine_tag",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "tag_to_refine": tag_to_refine,
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                },
                refine_tag_refine_params.RefineTagRefineParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefineTagRefineResponse,
        )


class AsyncRefineTagResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefineTagResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRefineTagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefineTagResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncRefineTagResourceWithStreamingResponse(self)

    async def refine(
        self,
        *,
        endpoint_manager_config: object,
        tag_to_refine: Dict[str, refine_tag_refine_params.TagToRefine],
        vector_db_config: object,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RefineTagRefineResponse:
        """
        Refine an existing tag by analyzing its previous extractions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/refine_tag",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "tag_to_refine": tag_to_refine,
                    "vector_db_config": vector_db_config,
                    "file_names": file_names,
                },
                refine_tag_refine_params.RefineTagRefineParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefineTagRefineResponse,
        )


class RefineTagResourceWithRawResponse:
    def __init__(self, refine_tag: RefineTagResource) -> None:
        self._refine_tag = refine_tag

        self.refine = to_raw_response_wrapper(
            refine_tag.refine,
        )


class AsyncRefineTagResourceWithRawResponse:
    def __init__(self, refine_tag: AsyncRefineTagResource) -> None:
        self._refine_tag = refine_tag

        self.refine = async_to_raw_response_wrapper(
            refine_tag.refine,
        )


class RefineTagResourceWithStreamingResponse:
    def __init__(self, refine_tag: RefineTagResource) -> None:
        self._refine_tag = refine_tag

        self.refine = to_streamed_response_wrapper(
            refine_tag.refine,
        )


class AsyncRefineTagResourceWithStreamingResponse:
    def __init__(self, refine_tag: AsyncRefineTagResource) -> None:
        self._refine_tag = refine_tag

        self.refine = async_to_streamed_response_wrapper(
            refine_tag.refine,
        )
