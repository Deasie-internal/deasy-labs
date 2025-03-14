# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import (
    graph_list_params,
    graph_create_params,
    graph_delete_params,
    graph_update_params,
    graph_upsert_params,
)
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
from ..types.graph_operation import GraphOperation
from ..types.graph_list_response import GraphListResponse

__all__ = ["GraphResource", "AsyncGraphResource"]


class GraphResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return GraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return GraphResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        graph_name: str,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """
        Create a new graph.

        Args: request: The request containing graph details (name, description, data).
        x_user_and_token_id: The authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the created graph ID.

        Raises: HTTPException: If there's an error creating the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/graph/create",
            body=maybe_transform(
                {
                    "graph_name": graph_name,
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                },
                graph_create_params.GraphCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphOperation,
        )

    def update(
        self,
        *,
        graph_name: str,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """
        Update a graph in the database.

        Args: request: The request containing graph details (name, description, data).
        x_user_and_token_id: The authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the upserted graph ID.

        Raises: HTTPException: If there's an error upserting the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/graph/update",
            body=maybe_transform(
                {
                    "graph_name": graph_name,
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                },
                graph_update_params.GraphUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphOperation,
        )

    def list(
        self,
        *,
        graph_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphListResponse:
        """
        List all graphs for the authenticated user.

        Args: request: The request containing optional filter by graph names.
        x_user_and_token_id: The authenticated user and token ID.

        Returns: ListGraphsResponse: The response containing the list of graphs.

        Raises: HTTPException: If there's an error retrieving the graphs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/graph/list",
            body=maybe_transform({"graph_names": graph_names}, graph_list_params.GraphListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphListResponse,
        )

    def delete(
        self,
        *,
        graph_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """Delete a graph by ID.

        Args: graph_id: The ID of the graph to delete.

        x_user_and_token_id: The
        authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the deleted graph ID.

        Raises: HTTPException: If there's an error deleting the graph.

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
                query=maybe_transform({"graph_name": graph_name}, graph_delete_params.GraphDeleteParams),
            ),
            cast_to=GraphOperation,
        )

    def upsert(
        self,
        *,
        graph_name: str,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        new_graph_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """
        Upsert a graph in the database.

        Creates a new graph if graph_id is None, otherwise updates an existing graph.

        Args: request: The request containing graph details (id, name, description,
        data). x_user_and_token_id: The authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the upserted graph ID.

        Raises: HTTPException: If there's an error upserting the graph.

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
                    "graph_name": graph_name,
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                    "new_graph_name": new_graph_name,
                },
                graph_upsert_params.GraphUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphOperation,
        )


class AsyncGraphResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncGraphResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        graph_name: str,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """
        Create a new graph.

        Args: request: The request containing graph details (name, description, data).
        x_user_and_token_id: The authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the created graph ID.

        Raises: HTTPException: If there's an error creating the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/graph/create",
            body=await async_maybe_transform(
                {
                    "graph_name": graph_name,
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                },
                graph_create_params.GraphCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphOperation,
        )

    async def update(
        self,
        *,
        graph_name: str,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """
        Update a graph in the database.

        Args: request: The request containing graph details (name, description, data).
        x_user_and_token_id: The authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the upserted graph ID.

        Raises: HTTPException: If there's an error upserting the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/graph/update",
            body=await async_maybe_transform(
                {
                    "graph_name": graph_name,
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                },
                graph_update_params.GraphUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphOperation,
        )

    async def list(
        self,
        *,
        graph_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphListResponse:
        """
        List all graphs for the authenticated user.

        Args: request: The request containing optional filter by graph names.
        x_user_and_token_id: The authenticated user and token ID.

        Returns: ListGraphsResponse: The response containing the list of graphs.

        Raises: HTTPException: If there's an error retrieving the graphs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/graph/list",
            body=await async_maybe_transform({"graph_names": graph_names}, graph_list_params.GraphListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphListResponse,
        )

    async def delete(
        self,
        *,
        graph_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """Delete a graph by ID.

        Args: graph_id: The ID of the graph to delete.

        x_user_and_token_id: The
        authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the deleted graph ID.

        Raises: HTTPException: If there's an error deleting the graph.

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
                query=await async_maybe_transform({"graph_name": graph_name}, graph_delete_params.GraphDeleteParams),
            ),
            cast_to=GraphOperation,
        )

    async def upsert(
        self,
        *,
        graph_name: str,
        graph_data: Optional[object] | NotGiven = NOT_GIVEN,
        graph_description: Optional[str] | NotGiven = NOT_GIVEN,
        new_graph_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphOperation:
        """
        Upsert a graph in the database.

        Creates a new graph if graph_id is None, otherwise updates an existing graph.

        Args: request: The request containing graph details (id, name, description,
        data). x_user_and_token_id: The authenticated user and token ID.

        Returns: GraphOperationResponse: The response containing the upserted graph ID.

        Raises: HTTPException: If there's an error upserting the graph.

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
                    "graph_name": graph_name,
                    "graph_data": graph_data,
                    "graph_description": graph_description,
                    "new_graph_name": new_graph_name,
                },
                graph_upsert_params.GraphUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphOperation,
        )


class GraphResourceWithRawResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.create = to_raw_response_wrapper(
            graph.create,
        )
        self.update = to_raw_response_wrapper(
            graph.update,
        )
        self.list = to_raw_response_wrapper(
            graph.list,
        )
        self.delete = to_raw_response_wrapper(
            graph.delete,
        )
        self.upsert = to_raw_response_wrapper(
            graph.upsert,
        )


class AsyncGraphResourceWithRawResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.create = async_to_raw_response_wrapper(
            graph.create,
        )
        self.update = async_to_raw_response_wrapper(
            graph.update,
        )
        self.list = async_to_raw_response_wrapper(
            graph.list,
        )
        self.delete = async_to_raw_response_wrapper(
            graph.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            graph.upsert,
        )


class GraphResourceWithStreamingResponse:
    def __init__(self, graph: GraphResource) -> None:
        self._graph = graph

        self.create = to_streamed_response_wrapper(
            graph.create,
        )
        self.update = to_streamed_response_wrapper(
            graph.update,
        )
        self.list = to_streamed_response_wrapper(
            graph.list,
        )
        self.delete = to_streamed_response_wrapper(
            graph.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            graph.upsert,
        )


class AsyncGraphResourceWithStreamingResponse:
    def __init__(self, graph: AsyncGraphResource) -> None:
        self._graph = graph

        self.create = async_to_streamed_response_wrapper(
            graph.create,
        )
        self.update = async_to_streamed_response_wrapper(
            graph.update,
        )
        self.list = async_to_streamed_response_wrapper(
            graph.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            graph.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            graph.upsert,
        )
