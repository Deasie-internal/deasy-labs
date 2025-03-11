# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import graph_list_params, graph_delete_params, graph_create_or_update_params
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
from ..types.graph_list_response import GraphListResponse
from ..types.graph_delete_response import GraphDeleteResponse
from ..types.graph_create_or_update_response import GraphCreateOrUpdateResponse

__all__ = ["GraphResource", "AsyncGraphResource"]


class GraphResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return GraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return GraphResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        graph_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphListResponse:
        """
        List all graphs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/graph/list",
            body=maybe_transform({"graph_ids": graph_ids}, graph_list_params.GraphListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphListResponse,
        )

    def delete(
        self,
        *,
        graph_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphDeleteResponse:
        """
        Delete a graph

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/graph/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"graph_id": graph_id}, graph_delete_params.GraphDeleteParams),
            ),
            cast_to=GraphDeleteResponse,
        )

    def create_or_update(
        self,
        *,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        graph_id: Optional[str] | NotGiven = NOT_GIVEN,
        graph_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphCreateOrUpdateResponse:
        """
        Create or update a graph in the database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/graph/upsert",
            body=maybe_transform(
                {
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                    "graph_id": graph_id,
                    "graph_name": graph_name,
                },
                graph_create_or_update_params.GraphCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphCreateOrUpdateResponse,
        )


class AsyncGraphResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncGraphResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        graph_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphListResponse:
        """
        List all graphs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/graph/list",
            body=await async_maybe_transform({"graph_ids": graph_ids}, graph_list_params.GraphListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphListResponse,
        )

    async def delete(
        self,
        *,
        graph_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphDeleteResponse:
        """
        Delete a graph

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/graph/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"graph_id": graph_id}, graph_delete_params.GraphDeleteParams),
            ),
            cast_to=GraphDeleteResponse,
        )

    async def create_or_update(
        self,
        *,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        graph_id: Optional[str] | NotGiven = NOT_GIVEN,
        graph_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphCreateOrUpdateResponse:
        """
        Create or update a graph in the database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/graph/upsert",
            body=await async_maybe_transform(
                {
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                    "graph_id": graph_id,
                    "graph_name": graph_name,
                },
                graph_create_or_update_params.GraphCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphCreateOrUpdateResponse,
        )


class GraphResourceWithRawResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.list = to_raw_response_wrapper(
            graph.list,
        )
        self.delete = to_raw_response_wrapper(
            graph.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            graph.create_or_update,
        )


class AsyncGraphResourceWithRawResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.list = async_to_raw_response_wrapper(
            graph.list,
        )
        self.delete = async_to_raw_response_wrapper(
            graph.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            graph.create_or_update,
        )


class GraphResourceWithStreamingResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.list = to_streamed_response_wrapper(
            graph.list,
        )
        self.delete = to_streamed_response_wrapper(
            graph.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            graph.create_or_update,
        )


class AsyncGraphResourceWithStreamingResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.list = async_to_streamed_response_wrapper(
            graph.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            graph.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            graph.create_or_update,
        )
