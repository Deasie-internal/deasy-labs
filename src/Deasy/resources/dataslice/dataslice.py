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
    dataslice_create_params,
    dataslice_delete_params,
    dataslice_get_files_params,
    dataslice_get_metrics_params,
    dataslice_get_file_count_params,
    dataslice_check_sync_score_params,
    dataslice_tag_vdb_distribution_params,
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
from ...types.condition_input_param import ConditionInputParam
from ...types.dataslice_list_response import DatasliceListResponse
from ...types.dataslice_create_response import DatasliceCreateResponse
from ...types.dataslice_delete_response import DatasliceDeleteResponse
from ...types.dataslice_get_files_response import DatasliceGetFilesResponse
from ...types.dataslice_get_metrics_response import DatasliceGetMetricsResponse
from ...types.dataslice_get_file_count_response import DatasliceGetFileCountResponse
from ...types.dataslice_check_sync_score_response import DatasliceCheckSyncScoreResponse
from ...types.dataslice_tag_vdb_distribution_response import DatasliceTagVdbDistributionResponse

__all__ = ["DatasliceResource", "AsyncDatasliceResource"]


class DatasliceResource(SyncAPIResource):
    @cached_property
    def export(self) -> ExportResource:
        return ExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasliceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return DatasliceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasliceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return DatasliceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataslice_name: str,
        graph_id: str,
        latest_graph: object,
        vdb_profile_name: str,
        condition: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        condition_new: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        data_points: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceCreateResponse:
        """
        Create a new use case based on given conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataslice/create",
            body=maybe_transform(
                {
                    "dataslice_name": dataslice_name,
                    "graph_id": graph_id,
                    "latest_graph": latest_graph,
                    "vdb_profile_name": vdb_profile_name,
                    "condition": condition,
                    "condition_new": condition_new,
                    "data_points": data_points,
                    "description": description,
                    "status": status,
                },
                dataslice_create_params.DatasliceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceCreateResponse,
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
    ) -> DatasliceListResponse:
        """List all dataslices"""
        return self._get(
            "/dataslice/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceListResponse,
        )

    def delete(
        self,
        *,
        dataslice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceDeleteResponse:
        """
        Delete a use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/dataslice/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataslice_id": dataslice_id}, dataslice_delete_params.DatasliceDeleteParams),
            ),
            cast_to=DatasliceDeleteResponse,
        )

    def check_sync_score(
        self,
        *,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        hard_limit: Optional[int] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceCheckSyncScoreResponse:
        """
        Check the synchronization status of a specific use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataslice/sync_score",
            body=maybe_transform(
                {
                    "dataslice_id": dataslice_id,
                    "hard_limit": hard_limit,
                    "vector_db_config": vector_db_config,
                },
                dataslice_check_sync_score_params.DatasliceCheckSyncScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceCheckSyncScoreResponse,
        )

    def get_file_count(
        self,
        *,
        condition: Iterable[object],
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        new_condition: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceGetFileCountResponse:
        """
        Get count of files matching dataslice conditions or provided conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataslice/file_count",
            body=maybe_transform(
                {
                    "condition": condition,
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "new_condition": new_condition,
                },
                dataslice_get_file_count_params.DatasliceGetFileCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceGetFileCountResponse,
        )

    def get_files(
        self,
        *,
        dataslice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceGetFilesResponse:
        """
        Get all files associated with a dataslice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataslice/files",
            body=maybe_transform({"dataslice_id": dataslice_id}, dataslice_get_files_params.DatasliceGetFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceGetFilesResponse,
        )

    def get_metrics(
        self,
        *,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        node_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceGetMetricsResponse:
        """
        Retrieve use case metrics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataslice/metrics",
            body=maybe_transform(
                {
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "node_ids": node_ids,
                    "tags": tags,
                    "vector_db_config": vector_db_config,
                },
                dataslice_get_metrics_params.DatasliceGetMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceGetMetricsResponse,
        )

    def tag_vdb_distribution(
        self,
        *,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceTagVdbDistributionResponse:
        """
        Get the distribution of tags in a dataslice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataslice/tag_vdb_distribution",
            body=maybe_transform(
                {
                    "dataslice_id": dataslice_id,
                    "vector_db_config": vector_db_config,
                },
                dataslice_tag_vdb_distribution_params.DatasliceTagVdbDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceTagVdbDistributionResponse,
        )


class AsyncDatasliceResource(AsyncAPIResource):
    @cached_property
    def export(self) -> AsyncExportResource:
        return AsyncExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasliceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasliceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasliceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncDatasliceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataslice_name: str,
        graph_id: str,
        latest_graph: object,
        vdb_profile_name: str,
        condition: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        condition_new: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        data_points: Optional[int] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceCreateResponse:
        """
        Create a new use case based on given conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataslice/create",
            body=await async_maybe_transform(
                {
                    "dataslice_name": dataslice_name,
                    "graph_id": graph_id,
                    "latest_graph": latest_graph,
                    "vdb_profile_name": vdb_profile_name,
                    "condition": condition,
                    "condition_new": condition_new,
                    "data_points": data_points,
                    "description": description,
                    "status": status,
                },
                dataslice_create_params.DatasliceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceCreateResponse,
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
    ) -> DatasliceListResponse:
        """List all dataslices"""
        return await self._get(
            "/dataslice/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceListResponse,
        )

    async def delete(
        self,
        *,
        dataslice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceDeleteResponse:
        """
        Delete a use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/dataslice/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataslice_id": dataslice_id}, dataslice_delete_params.DatasliceDeleteParams
                ),
            ),
            cast_to=DatasliceDeleteResponse,
        )

    async def check_sync_score(
        self,
        *,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        hard_limit: Optional[int] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceCheckSyncScoreResponse:
        """
        Check the synchronization status of a specific use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataslice/sync_score",
            body=await async_maybe_transform(
                {
                    "dataslice_id": dataslice_id,
                    "hard_limit": hard_limit,
                    "vector_db_config": vector_db_config,
                },
                dataslice_check_sync_score_params.DatasliceCheckSyncScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceCheckSyncScoreResponse,
        )

    async def get_file_count(
        self,
        *,
        condition: Iterable[object],
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        new_condition: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceGetFileCountResponse:
        """
        Get count of files matching dataslice conditions or provided conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataslice/file_count",
            body=await async_maybe_transform(
                {
                    "condition": condition,
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "new_condition": new_condition,
                },
                dataslice_get_file_count_params.DatasliceGetFileCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceGetFileCountResponse,
        )

    async def get_files(
        self,
        *,
        dataslice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceGetFilesResponse:
        """
        Get all files associated with a dataslice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataslice/files",
            body=await async_maybe_transform(
                {"dataslice_id": dataslice_id}, dataslice_get_files_params.DatasliceGetFilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceGetFilesResponse,
        )

    async def get_metrics(
        self,
        *,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        node_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceGetMetricsResponse:
        """
        Retrieve use case metrics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataslice/metrics",
            body=await async_maybe_transform(
                {
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "node_ids": node_ids,
                    "tags": tags,
                    "vector_db_config": vector_db_config,
                },
                dataslice_get_metrics_params.DatasliceGetMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceGetMetricsResponse,
        )

    async def tag_vdb_distribution(
        self,
        *,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasliceTagVdbDistributionResponse:
        """
        Get the distribution of tags in a dataslice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataslice/tag_vdb_distribution",
            body=await async_maybe_transform(
                {
                    "dataslice_id": dataslice_id,
                    "vector_db_config": vector_db_config,
                },
                dataslice_tag_vdb_distribution_params.DatasliceTagVdbDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasliceTagVdbDistributionResponse,
        )


class DatasliceResourceWithRawResponse:
    def __init__(self, dataslice: DatasliceResource) -> None:
        self._dataslice = dataslice

        self.create = to_raw_response_wrapper(
            dataslice.create,
        )
        self.list = to_raw_response_wrapper(
            dataslice.list,
        )
        self.delete = to_raw_response_wrapper(
            dataslice.delete,
        )
        self.check_sync_score = to_raw_response_wrapper(
            dataslice.check_sync_score,
        )
        self.get_file_count = to_raw_response_wrapper(
            dataslice.get_file_count,
        )
        self.get_files = to_raw_response_wrapper(
            dataslice.get_files,
        )
        self.get_metrics = to_raw_response_wrapper(
            dataslice.get_metrics,
        )
        self.tag_vdb_distribution = to_raw_response_wrapper(
            dataslice.tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> ExportResourceWithRawResponse:
        return ExportResourceWithRawResponse(self._dataslice.export)


class AsyncDatasliceResourceWithRawResponse:
    def __init__(self, dataslice: AsyncDatasliceResource) -> None:
        self._dataslice = dataslice

        self.create = async_to_raw_response_wrapper(
            dataslice.create,
        )
        self.list = async_to_raw_response_wrapper(
            dataslice.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dataslice.delete,
        )
        self.check_sync_score = async_to_raw_response_wrapper(
            dataslice.check_sync_score,
        )
        self.get_file_count = async_to_raw_response_wrapper(
            dataslice.get_file_count,
        )
        self.get_files = async_to_raw_response_wrapper(
            dataslice.get_files,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            dataslice.get_metrics,
        )
        self.tag_vdb_distribution = async_to_raw_response_wrapper(
            dataslice.tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> AsyncExportResourceWithRawResponse:
        return AsyncExportResourceWithRawResponse(self._dataslice.export)


class DatasliceResourceWithStreamingResponse:
    def __init__(self, dataslice: DatasliceResource) -> None:
        self._dataslice = dataslice

        self.create = to_streamed_response_wrapper(
            dataslice.create,
        )
        self.list = to_streamed_response_wrapper(
            dataslice.list,
        )
        self.delete = to_streamed_response_wrapper(
            dataslice.delete,
        )
        self.check_sync_score = to_streamed_response_wrapper(
            dataslice.check_sync_score,
        )
        self.get_file_count = to_streamed_response_wrapper(
            dataslice.get_file_count,
        )
        self.get_files = to_streamed_response_wrapper(
            dataslice.get_files,
        )
        self.get_metrics = to_streamed_response_wrapper(
            dataslice.get_metrics,
        )
        self.tag_vdb_distribution = to_streamed_response_wrapper(
            dataslice.tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> ExportResourceWithStreamingResponse:
        return ExportResourceWithStreamingResponse(self._dataslice.export)


class AsyncDatasliceResourceWithStreamingResponse:
    def __init__(self, dataslice: AsyncDatasliceResource) -> None:
        self._dataslice = dataslice

        self.create = async_to_streamed_response_wrapper(
            dataslice.create,
        )
        self.list = async_to_streamed_response_wrapper(
            dataslice.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dataslice.delete,
        )
        self.check_sync_score = async_to_streamed_response_wrapper(
            dataslice.check_sync_score,
        )
        self.get_file_count = async_to_streamed_response_wrapper(
            dataslice.get_file_count,
        )
        self.get_files = async_to_streamed_response_wrapper(
            dataslice.get_files,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            dataslice.get_metrics,
        )
        self.tag_vdb_distribution = async_to_streamed_response_wrapper(
            dataslice.tag_vdb_distribution,
        )

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self._dataslice.export)
