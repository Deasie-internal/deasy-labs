# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from .export import (
    ExportResource,
    AsyncExportResource,
    ExportResourceWithRawResponse,
    AsyncExportResourceWithRawResponse,
    ExportResourceWithStreamingResponse,
    AsyncExportResourceWithStreamingResponse,
)
from ...types import (
    usecase_create_params,
    usecase_delete_params,
    usecase_get_files_params,
    usecase_check_sync_params,
    usecase_get_metrics_params,
    usecase_get_file_count_params,
    usecase_get_tag_vdb_distribution_params,
)
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
from ...types.condition_param import ConditionParam
from ...types.usecase_list_response import UsecaseListResponse
from ...types.usecase_create_response import UsecaseCreateResponse
from ...types.usecase_delete_response import UsecaseDeleteResponse
from ...types.usecase_get_files_response import UsecaseGetFilesResponse
from ...types.usecase_check_sync_response import UsecaseCheckSyncResponse
from ...types.usecase_get_metrics_response import UsecaseGetMetricsResponse
from ...types.usecase_get_file_count_response import UsecaseGetFileCountResponse
from ...types.usecase_get_tag_vdb_distribution_response import UsecaseGetTagVdbDistributionResponse

__all__ = ["UsecaseResource", "AsyncUsecaseResource"]


class UsecaseResource(SyncAPIResource):
    @cached_property
    def export(self) -> ExportResource:
        return ExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsecaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return UsecaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsecaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return UsecaseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        condition: Iterable[object],
        data_points: int,
        description: str,
        graph_id: str,
        last_updated: str,
        latest_graph: object,
        status: str,
        usecase_id: str,
        usecase_name: str,
        user_id: str,
        vector_db_config: object,
        condition_new: ConditionParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseCreateResponse:
        """
        Create a new use case based on given conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/create",
            body=maybe_transform(
                {
                    "condition": condition,
                    "data_points": data_points,
                    "description": description,
                    "graph_id": graph_id,
                    "last_updated": last_updated,
                    "latest_graph": latest_graph,
                    "status": status,
                    "usecase_id": usecase_id,
                    "usecase_name": usecase_name,
                    "user_id": user_id,
                    "vector_db_config": vector_db_config,
                    "condition_new": condition_new,
                },
                usecase_create_params.UsecaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseListResponse:
        """List all usecases"""
        return self._get(
            "/usecase/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseListResponse,
        )

    def delete(
        self,
        *,
        usecase_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseDeleteResponse:
        """
        Delete a use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/usecase/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"usecase_id": usecase_id}, usecase_delete_params.UsecaseDeleteParams),
            ),
            cast_to=UsecaseDeleteResponse,
        )

    def check_sync(
        self,
        *,
        hard_limit: Optional[int] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseCheckSyncResponse:
        """
        Check the synchronization status of a specific use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/sync_score",
            body=maybe_transform(
                {
                    "hard_limit": hard_limit,
                    "usecase_id": usecase_id,
                    "vector_db_config": vector_db_config,
                },
                usecase_check_sync_params.UsecaseCheckSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseCheckSyncResponse,
        )

    def get_file_count(
        self,
        *,
        condition: Iterable[object],
        vector_db_config: object,
        new_condition: Optional[ConditionParam] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetFileCountResponse:
        """
        Get count of files matching usecase conditions or provided conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/file_count",
            body=maybe_transform(
                {
                    "condition": condition,
                    "vector_db_config": vector_db_config,
                    "new_condition": new_condition,
                    "usecase_id": usecase_id,
                },
                usecase_get_file_count_params.UsecaseGetFileCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetFileCountResponse,
        )

    def get_files(
        self,
        *,
        usecase_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetFilesResponse:
        """
        Get all files associated with a usecase

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/files",
            body=maybe_transform({"usecase_id": usecase_id}, usecase_get_files_params.UsecaseGetFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetFilesResponse,
        )

    def get_metrics(
        self,
        *,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        node_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetMetricsResponse:
        """
        Retrieve use case metrics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/metrics",
            body=maybe_transform(
                {
                    "file_names": file_names,
                    "node_ids": node_ids,
                    "tags": tags,
                    "usecase_id": usecase_id,
                    "vector_db_config": vector_db_config,
                },
                usecase_get_metrics_params.UsecaseGetMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetMetricsResponse,
        )

    def get_tag_vdb_distribution(
        self,
        *,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetTagVdbDistributionResponse:
        """
        Get the distribution of tags in a usecase

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/tag_vdb_distribution",
            body=maybe_transform(
                {
                    "usecase_id": usecase_id,
                    "vector_db_config": vector_db_config,
                },
                usecase_get_tag_vdb_distribution_params.UsecaseGetTagVdbDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetTagVdbDistributionResponse,
        )


class AsyncUsecaseResource(AsyncAPIResource):
    @cached_property
    def export(self) -> AsyncExportResource:
        return AsyncExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsecaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsecaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsecaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncUsecaseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        condition: Iterable[object],
        data_points: int,
        description: str,
        graph_id: str,
        last_updated: str,
        latest_graph: object,
        status: str,
        usecase_id: str,
        usecase_name: str,
        user_id: str,
        vector_db_config: object,
        condition_new: ConditionParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseCreateResponse:
        """
        Create a new use case based on given conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/create",
            body=await async_maybe_transform(
                {
                    "condition": condition,
                    "data_points": data_points,
                    "description": description,
                    "graph_id": graph_id,
                    "last_updated": last_updated,
                    "latest_graph": latest_graph,
                    "status": status,
                    "usecase_id": usecase_id,
                    "usecase_name": usecase_name,
                    "user_id": user_id,
                    "vector_db_config": vector_db_config,
                    "condition_new": condition_new,
                },
                usecase_create_params.UsecaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseListResponse:
        """List all usecases"""
        return await self._get(
            "/usecase/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseListResponse,
        )

    async def delete(
        self,
        *,
        usecase_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseDeleteResponse:
        """
        Delete a use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/usecase/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"usecase_id": usecase_id}, usecase_delete_params.UsecaseDeleteParams
                ),
            ),
            cast_to=UsecaseDeleteResponse,
        )

    async def check_sync(
        self,
        *,
        hard_limit: Optional[int] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseCheckSyncResponse:
        """
        Check the synchronization status of a specific use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/sync_score",
            body=await async_maybe_transform(
                {
                    "hard_limit": hard_limit,
                    "usecase_id": usecase_id,
                    "vector_db_config": vector_db_config,
                },
                usecase_check_sync_params.UsecaseCheckSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseCheckSyncResponse,
        )

    async def get_file_count(
        self,
        *,
        condition: Iterable[object],
        vector_db_config: object,
        new_condition: Optional[ConditionParam] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetFileCountResponse:
        """
        Get count of files matching usecase conditions or provided conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/file_count",
            body=await async_maybe_transform(
                {
                    "condition": condition,
                    "vector_db_config": vector_db_config,
                    "new_condition": new_condition,
                    "usecase_id": usecase_id,
                },
                usecase_get_file_count_params.UsecaseGetFileCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetFileCountResponse,
        )

    async def get_files(
        self,
        *,
        usecase_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetFilesResponse:
        """
        Get all files associated with a usecase

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/files",
            body=await async_maybe_transform(
                {"usecase_id": usecase_id}, usecase_get_files_params.UsecaseGetFilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetFilesResponse,
        )

    async def get_metrics(
        self,
        *,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        node_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetMetricsResponse:
        """
        Retrieve use case metrics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/metrics",
            body=await async_maybe_transform(
                {
                    "file_names": file_names,
                    "node_ids": node_ids,
                    "tags": tags,
                    "usecase_id": usecase_id,
                    "vector_db_config": vector_db_config,
                },
                usecase_get_metrics_params.UsecaseGetMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetMetricsResponse,
        )

    async def get_tag_vdb_distribution(
        self,
        *,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsecaseGetTagVdbDistributionResponse:
        """
        Get the distribution of tags in a usecase

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/tag_vdb_distribution",
            body=await async_maybe_transform(
                {
                    "usecase_id": usecase_id,
                    "vector_db_config": vector_db_config,
                },
                usecase_get_tag_vdb_distribution_params.UsecaseGetTagVdbDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsecaseGetTagVdbDistributionResponse,
        )


class UsecaseResourceWithRawResponse:
    def __init__(self, usecase: UsecaseResource) -> None:
        self._usecase = usecase

        self.create = to_raw_response_wrapper(
            usecase.create,
        )
        self.list = to_raw_response_wrapper(
            usecase.list,
        )
        self.delete = to_raw_response_wrapper(
            usecase.delete,
        )
        self.check_sync = to_raw_response_wrapper(
            usecase.check_sync,
        )
        self.get_file_count = to_raw_response_wrapper(
            usecase.get_file_count,
        )
        self.get_files = to_raw_response_wrapper(
            usecase.get_files,
        )
        self.get_metrics = to_raw_response_wrapper(
            usecase.get_metrics,
        )
        self.get_tag_vdb_distribution = to_raw_response_wrapper(
            usecase.get_tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> ExportResourceWithRawResponse:
        return ExportResourceWithRawResponse(self._usecase.export)


class AsyncUsecaseResourceWithRawResponse:
    def __init__(self, usecase: AsyncUsecaseResource) -> None:
        self._usecase = usecase

        self.create = async_to_raw_response_wrapper(
            usecase.create,
        )
        self.list = async_to_raw_response_wrapper(
            usecase.list,
        )
        self.delete = async_to_raw_response_wrapper(
            usecase.delete,
        )
        self.check_sync = async_to_raw_response_wrapper(
            usecase.check_sync,
        )
        self.get_file_count = async_to_raw_response_wrapper(
            usecase.get_file_count,
        )
        self.get_files = async_to_raw_response_wrapper(
            usecase.get_files,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            usecase.get_metrics,
        )
        self.get_tag_vdb_distribution = async_to_raw_response_wrapper(
            usecase.get_tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> AsyncExportResourceWithRawResponse:
        return AsyncExportResourceWithRawResponse(self._usecase.export)


class UsecaseResourceWithStreamingResponse:
    def __init__(self, usecase: UsecaseResource) -> None:
        self._usecase = usecase

        self.create = to_streamed_response_wrapper(
            usecase.create,
        )
        self.list = to_streamed_response_wrapper(
            usecase.list,
        )
        self.delete = to_streamed_response_wrapper(
            usecase.delete,
        )
        self.check_sync = to_streamed_response_wrapper(
            usecase.check_sync,
        )
        self.get_file_count = to_streamed_response_wrapper(
            usecase.get_file_count,
        )
        self.get_files = to_streamed_response_wrapper(
            usecase.get_files,
        )
        self.get_metrics = to_streamed_response_wrapper(
            usecase.get_metrics,
        )
        self.get_tag_vdb_distribution = to_streamed_response_wrapper(
            usecase.get_tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> ExportResourceWithStreamingResponse:
        return ExportResourceWithStreamingResponse(self._usecase.export)


class AsyncUsecaseResourceWithStreamingResponse:
    def __init__(self, usecase: AsyncUsecaseResource) -> None:
        self._usecase = usecase

        self.create = async_to_streamed_response_wrapper(
            usecase.create,
        )
        self.list = async_to_streamed_response_wrapper(
            usecase.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            usecase.delete,
        )
        self.check_sync = async_to_streamed_response_wrapper(
            usecase.check_sync,
        )
        self.get_file_count = async_to_streamed_response_wrapper(
            usecase.get_file_count,
        )
        self.get_files = async_to_streamed_response_wrapper(
            usecase.get_files,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            usecase.get_metrics,
        )
        self.get_tag_vdb_distribution = async_to_streamed_response_wrapper(
            usecase.get_tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self._usecase.export)
