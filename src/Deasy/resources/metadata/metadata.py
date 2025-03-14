# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

from .file import (
    FileResource,
    AsyncFileResource,
    FileResourceWithRawResponse,
    AsyncFileResourceWithRawResponse,
    FileResourceWithStreamingResponse,
    AsyncFileResourceWithStreamingResponse,
)
from .chunk import (
    ChunkResource,
    AsyncChunkResource,
    ChunkResourceWithRawResponse,
    AsyncChunkResourceWithRawResponse,
    ChunkResourceWithStreamingResponse,
    AsyncChunkResourceWithStreamingResponse,
)
from ...types import (
    metadata_delete_params,
    metadata_get_evidence_params,
    metadata_get_unique_tags_params,
    metadata_get_distributions_params,
    metadata_get_basic_metadata_params,
    metadata_get_tag_statistics_params,
    metadata_count_distributions_params,
    metadata_get_distinct_values_params,
    metadata_filter_by_conditions_params,
    metadata_get_filtered_metadata_params,
    metadata_suggest_standardization_params,
    metadata_apply_standardization_db_params,
    metadata_get_oob_tagged_file_count_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
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
from .standardize import (
    StandardizeResource,
    AsyncStandardizeResource,
    StandardizeResourceWithRawResponse,
    AsyncStandardizeResourceWithRawResponse,
    StandardizeResourceWithStreamingResponse,
    AsyncStandardizeResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.condition_param import ConditionParam
from ...types.tag_condition_param import TagConditionParam
from ...types.metadata_delete_response import MetadataDeleteResponse
from ...types.metadata_get_evidence_response import MetadataGetEvidenceResponse
from ...types.metadata_get_unique_tags_response import MetadataGetUniqueTagsResponse
from ...types.metadata_get_distributions_response import MetadataGetDistributionsResponse
from ...types.metadata_get_basic_metadata_response import MetadataGetBasicMetadataResponse
from ...types.metadata_get_tag_statistics_response import MetadataGetTagStatisticsResponse
from ...types.metadata_count_distributions_response import MetadataCountDistributionsResponse
from ...types.metadata_get_distinct_values_response import MetadataGetDistinctValuesResponse
from ...types.metadata_filter_by_conditions_response import MetadataFilterByConditionsResponse
from ...types.metadata_get_filtered_metadata_response import MetadataGetFilteredMetadataResponse
from ...types.metadata_suggest_standardization_response import MetadataSuggestStandardizationResponse
from ...types.metadata_apply_standardization_db_response import MetadataApplyStandardizationDBResponse
from ...types.metadata_get_oob_tagged_file_count_response import MetadataGetOobTaggedFileCountResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def file(self) -> FileResource:
        return FileResource(self._client)

    @cached_property
    def chunk(self) -> ChunkResource:
        return ChunkResource(self._client)

    @cached_property
    def standardize(self) -> StandardizeResource:
        return StandardizeResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        conditions: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataDeleteResponse:
        """
        Delete metadata for specified files and tags from the chunk-level metadata table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/metadata/delete",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "file_names": file_names,
                    "tags": tags,
                },
                metadata_delete_params.MetadataDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataDeleteResponse,
        )

    def apply_standardization_db(
        self,
        *,
        endpoint_manager_config: object,
        standard_mapping: Dict[str, Iterable[object]],
        tag_name: str,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataApplyStandardizationDBResponse:
        """
        Apply standardization mapping to metadata values in database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/standardization_db",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "standard_mapping": standard_mapping,
                    "tag_name": tag_name,
                    "vector_db_config": vector_db_config,
                },
                metadata_apply_standardization_db_params.MetadataApplyStandardizationDBParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataApplyStandardizationDBResponse,
        )

    def count_distributions(
        self,
        *,
        current_tree: str,
        vector_db_config: object,
        conditions: Iterable[metadata_count_distributions_params.Condition] | NotGiven = NOT_GIVEN,
        endpoint_manager_config: Optional[object] | NotGiven = NOT_GIVEN,
        x_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataCountDistributionsResponse:
        """
        Get file count distributions for a hierarchy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-token": x_token}), **(extra_headers or {})}
        return self._post(
            "/metadata/count_distributions",
            body=maybe_transform(
                {
                    "current_tree": current_tree,
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "endpoint_manager_config": endpoint_manager_config,
                },
                metadata_count_distributions_params.MetadataCountDistributionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataCountDistributionsResponse,
        )

    def filter_by_conditions(
        self,
        *,
        conditions: Iterable[TagConditionParam],
        vector_db_config: object,
        analyze_remaining_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataFilterByConditionsResponse:
        """
        Filter files based on metadata conditions and get statistics about the filtered
        set

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/conditional_filter",
            body=maybe_transform(
                {
                    "conditions": conditions,
                    "vector_db_config": vector_db_config,
                    "analyze_remaining_tags": analyze_remaining_tags,
                },
                metadata_filter_by_conditions_params.MetadataFilterByConditionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataFilterByConditionsResponse,
        )

    def get_basic_metadata(
        self,
        *,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetBasicMetadataResponse:
        """
        Get unique values for each metadata tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/basic",
            body=maybe_transform(
                {"vector_db_config": vector_db_config},
                metadata_get_basic_metadata_params.MetadataGetBasicMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetBasicMetadataResponse,
        )

    def get_distinct_values(
        self,
        *,
        page: int,
        tag_id: str,
        vector_db_config: object,
        x_user: str,
        conditions: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        per_page: Optional[int] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetDistinctValuesResponse:
        """
        Get distinct values for a specific metadata tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/metadata/distinct_values",
            body=maybe_transform(
                {
                    "page": page,
                    "tag_id": tag_id,
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "per_page": per_page,
                    "search_query": search_query,
                },
                metadata_get_distinct_values_params.MetadataGetDistinctValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetDistinctValuesResponse,
        )

    def get_distributions(
        self,
        *,
        vector_db_config: object,
        columns: Optional[List[str]] | NotGiven = NOT_GIVEN,
        conditions_new: Optional[ConditionParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        max_val_per_tag: Optional[int] | NotGiven = NOT_GIVEN,
        node_condition: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetDistributionsResponse:
        """
        Get distribution counts for all metadata tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/distributions",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "columns": columns,
                    "conditions_new": conditions_new,
                    "dataslice_id": dataslice_id,
                    "max_val_per_tag": max_val_per_tag,
                    "node_condition": node_condition,
                },
                metadata_get_distributions_params.MetadataGetDistributionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetDistributionsResponse,
        )

    def get_evidence(
        self,
        *,
        filename: str,
        tag_id: str,
        tag_value: str,
        vector_db_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetEvidenceResponse:
        """
        Retrieve evidence for specified file and tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return self._post(
            "/metadata/get_evidence",
            body=maybe_transform(
                {
                    "filename": filename,
                    "tag_id": tag_id,
                    "tag_value": tag_value,
                    "vector_db_config": vector_db_config,
                },
                metadata_get_evidence_params.MetadataGetEvidenceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetEvidenceResponse,
        )

    def get_filtered_metadata(
        self,
        *,
        conditions: Iterable[metadata_get_filtered_metadata_params.Condition],
        vector_db_config: object,
        conditions_new: Optional[ConditionParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        node_condition: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        sort_by: Optional[str] | NotGiven = NOT_GIVEN,
        sort_order: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetFilteredMetadataResponse:
        """
        Get paginated filtered metadata based on conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/filtered",
            body=maybe_transform(
                {
                    "conditions": conditions,
                    "vector_db_config": vector_db_config,
                    "conditions_new": conditions_new,
                    "dataslice_id": dataslice_id,
                    "limit": limit,
                    "node_condition": node_condition,
                    "offset": offset,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                metadata_get_filtered_metadata_params.MetadataGetFilteredMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetFilteredMetadataResponse,
        )

    def get_oob_tagged_file_count(
        self,
        *,
        vector_db_config: object,
        conditions: Iterable[TagConditionParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetOobTaggedFileCountResponse:
        """
        Get statistics about OOB tag coverage across files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/oob_tag_file_count",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                },
                metadata_get_oob_tagged_file_count_params.MetadataGetOobTaggedFileCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetOobTaggedFileCountResponse,
        )

    def get_tag_statistics(
        self,
        *,
        vector_db_config: object,
        conditions: Iterable[TagConditionParam] | NotGiven = NOT_GIVEN,
        tag_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetTagStatisticsResponse:
        """
        Get statistics about metadata extractions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/tag_statistics",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "tag_ids": tag_ids,
                },
                metadata_get_tag_statistics_params.MetadataGetTagStatisticsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetTagStatisticsResponse,
        )

    def get_unique_tags(
        self,
        *,
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        node_condition: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetUniqueTagsResponse:
        """
        Get a list of unique tags that have been extracted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/get_unique_tags",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "node_condition": node_condition,
                },
                metadata_get_unique_tags_params.MetadataGetUniqueTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetUniqueTagsResponse,
        )

    def suggest_standardization(
        self,
        *,
        description: str,
        endpoint_manager_config: object,
        output_type: str,
        tag_name: str,
        value_distribution: Dict[str, float],
        vector_db_config: object,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        existing_categories: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataSuggestStandardizationResponse:
        """
        Standardize metadata values using LLM

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/metadata/standardization_suggest",
            body=maybe_transform(
                {
                    "description": description,
                    "endpoint_manager_config": endpoint_manager_config,
                    "output_type": output_type,
                    "tag_name": tag_name,
                    "value_distribution": value_distribution,
                    "vector_db_config": vector_db_config,
                    "context": context,
                    "existing_categories": existing_categories,
                },
                metadata_suggest_standardization_params.MetadataSuggestStandardizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataSuggestStandardizationResponse,
        )


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def file(self) -> AsyncFileResource:
        return AsyncFileResource(self._client)

    @cached_property
    def chunk(self) -> AsyncChunkResource:
        return AsyncChunkResource(self._client)

    @cached_property
    def standardize(self) -> AsyncStandardizeResource:
        return AsyncStandardizeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        vector_db_config: object,
        x_user: str,
        conditions: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataDeleteResponse:
        """
        Delete metadata for specified files and tags from the chunk-level metadata table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/metadata/delete",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "file_names": file_names,
                    "tags": tags,
                },
                metadata_delete_params.MetadataDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataDeleteResponse,
        )

    async def apply_standardization_db(
        self,
        *,
        endpoint_manager_config: object,
        standard_mapping: Dict[str, Iterable[object]],
        tag_name: str,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataApplyStandardizationDBResponse:
        """
        Apply standardization mapping to metadata values in database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/standardization_db",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "standard_mapping": standard_mapping,
                    "tag_name": tag_name,
                    "vector_db_config": vector_db_config,
                },
                metadata_apply_standardization_db_params.MetadataApplyStandardizationDBParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataApplyStandardizationDBResponse,
        )

    async def count_distributions(
        self,
        *,
        current_tree: str,
        vector_db_config: object,
        conditions: Iterable[metadata_count_distributions_params.Condition] | NotGiven = NOT_GIVEN,
        endpoint_manager_config: Optional[object] | NotGiven = NOT_GIVEN,
        x_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataCountDistributionsResponse:
        """
        Get file count distributions for a hierarchy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-token": x_token}), **(extra_headers or {})}
        return await self._post(
            "/metadata/count_distributions",
            body=await async_maybe_transform(
                {
                    "current_tree": current_tree,
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "endpoint_manager_config": endpoint_manager_config,
                },
                metadata_count_distributions_params.MetadataCountDistributionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataCountDistributionsResponse,
        )

    async def filter_by_conditions(
        self,
        *,
        conditions: Iterable[TagConditionParam],
        vector_db_config: object,
        analyze_remaining_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataFilterByConditionsResponse:
        """
        Filter files based on metadata conditions and get statistics about the filtered
        set

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/conditional_filter",
            body=await async_maybe_transform(
                {
                    "conditions": conditions,
                    "vector_db_config": vector_db_config,
                    "analyze_remaining_tags": analyze_remaining_tags,
                },
                metadata_filter_by_conditions_params.MetadataFilterByConditionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataFilterByConditionsResponse,
        )

    async def get_basic_metadata(
        self,
        *,
        vector_db_config: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetBasicMetadataResponse:
        """
        Get unique values for each metadata tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/basic",
            body=await async_maybe_transform(
                {"vector_db_config": vector_db_config},
                metadata_get_basic_metadata_params.MetadataGetBasicMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetBasicMetadataResponse,
        )

    async def get_distinct_values(
        self,
        *,
        page: int,
        tag_id: str,
        vector_db_config: object,
        x_user: str,
        conditions: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        per_page: Optional[int] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetDistinctValuesResponse:
        """
        Get distinct values for a specific metadata tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/metadata/distinct_values",
            body=await async_maybe_transform(
                {
                    "page": page,
                    "tag_id": tag_id,
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "per_page": per_page,
                    "search_query": search_query,
                },
                metadata_get_distinct_values_params.MetadataGetDistinctValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetDistinctValuesResponse,
        )

    async def get_distributions(
        self,
        *,
        vector_db_config: object,
        columns: Optional[List[str]] | NotGiven = NOT_GIVEN,
        conditions_new: Optional[ConditionParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        max_val_per_tag: Optional[int] | NotGiven = NOT_GIVEN,
        node_condition: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetDistributionsResponse:
        """
        Get distribution counts for all metadata tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/distributions",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "columns": columns,
                    "conditions_new": conditions_new,
                    "dataslice_id": dataslice_id,
                    "max_val_per_tag": max_val_per_tag,
                    "node_condition": node_condition,
                },
                metadata_get_distributions_params.MetadataGetDistributionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetDistributionsResponse,
        )

    async def get_evidence(
        self,
        *,
        filename: str,
        tag_id: str,
        tag_value: str,
        vector_db_config: object,
        x_user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetEvidenceResponse:
        """
        Retrieve evidence for specified file and tag

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-user": x_user, **(extra_headers or {})}
        return await self._post(
            "/metadata/get_evidence",
            body=await async_maybe_transform(
                {
                    "filename": filename,
                    "tag_id": tag_id,
                    "tag_value": tag_value,
                    "vector_db_config": vector_db_config,
                },
                metadata_get_evidence_params.MetadataGetEvidenceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetEvidenceResponse,
        )

    async def get_filtered_metadata(
        self,
        *,
        conditions: Iterable[metadata_get_filtered_metadata_params.Condition],
        vector_db_config: object,
        conditions_new: Optional[ConditionParam] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        node_condition: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        search_query: Optional[str] | NotGiven = NOT_GIVEN,
        sort_by: Optional[str] | NotGiven = NOT_GIVEN,
        sort_order: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetFilteredMetadataResponse:
        """
        Get paginated filtered metadata based on conditions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/filtered",
            body=await async_maybe_transform(
                {
                    "conditions": conditions,
                    "vector_db_config": vector_db_config,
                    "conditions_new": conditions_new,
                    "dataslice_id": dataslice_id,
                    "limit": limit,
                    "node_condition": node_condition,
                    "offset": offset,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                metadata_get_filtered_metadata_params.MetadataGetFilteredMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetFilteredMetadataResponse,
        )

    async def get_oob_tagged_file_count(
        self,
        *,
        vector_db_config: object,
        conditions: Iterable[TagConditionParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetOobTaggedFileCountResponse:
        """
        Get statistics about OOB tag coverage across files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/oob_tag_file_count",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                },
                metadata_get_oob_tagged_file_count_params.MetadataGetOobTaggedFileCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetOobTaggedFileCountResponse,
        )

    async def get_tag_statistics(
        self,
        *,
        vector_db_config: object,
        conditions: Iterable[TagConditionParam] | NotGiven = NOT_GIVEN,
        tag_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetTagStatisticsResponse:
        """
        Get statistics about metadata extractions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/tag_statistics",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "tag_ids": tag_ids,
                },
                metadata_get_tag_statistics_params.MetadataGetTagStatisticsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetTagStatisticsResponse,
        )

    async def get_unique_tags(
        self,
        *,
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        node_condition: Optional[Iterable[TagConditionParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataGetUniqueTagsResponse:
        """
        Get a list of unique tags that have been extracted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/get_unique_tags",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "node_condition": node_condition,
                },
                metadata_get_unique_tags_params.MetadataGetUniqueTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataGetUniqueTagsResponse,
        )

    async def suggest_standardization(
        self,
        *,
        description: str,
        endpoint_manager_config: object,
        output_type: str,
        tag_name: str,
        value_distribution: Dict[str, float],
        vector_db_config: object,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        existing_categories: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetadataSuggestStandardizationResponse:
        """
        Standardize metadata values using LLM

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/metadata/standardization_suggest",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "endpoint_manager_config": endpoint_manager_config,
                    "output_type": output_type,
                    "tag_name": tag_name,
                    "value_distribution": value_distribution,
                    "vector_db_config": vector_db_config,
                    "context": context,
                    "existing_categories": existing_categories,
                },
                metadata_suggest_standardization_params.MetadataSuggestStandardizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetadataSuggestStandardizationResponse,
        )


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.delete = to_raw_response_wrapper(
            metadata.delete,
        )
        self.apply_standardization_db = to_raw_response_wrapper(
            metadata.apply_standardization_db,
        )
        self.count_distributions = to_raw_response_wrapper(
            metadata.count_distributions,
        )
        self.filter_by_conditions = to_raw_response_wrapper(
            metadata.filter_by_conditions,
        )
        self.get_basic_metadata = to_raw_response_wrapper(
            metadata.get_basic_metadata,
        )
        self.get_distinct_values = to_raw_response_wrapper(
            metadata.get_distinct_values,
        )
        self.get_distributions = to_raw_response_wrapper(
            metadata.get_distributions,
        )
        self.get_evidence = to_raw_response_wrapper(
            metadata.get_evidence,
        )
        self.get_filtered_metadata = to_raw_response_wrapper(
            metadata.get_filtered_metadata,
        )
        self.get_oob_tagged_file_count = to_raw_response_wrapper(
            metadata.get_oob_tagged_file_count,
        )
        self.get_tag_statistics = to_raw_response_wrapper(
            metadata.get_tag_statistics,
        )
        self.get_unique_tags = to_raw_response_wrapper(
            metadata.get_unique_tags,
        )
        self.suggest_standardization = to_raw_response_wrapper(
            metadata.suggest_standardization,
        )

    @cached_property
    def file(self) -> FileResourceWithRawResponse:
        return FileResourceWithRawResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> ChunkResourceWithRawResponse:
        return ChunkResourceWithRawResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> StandardizeResourceWithRawResponse:
        return StandardizeResourceWithRawResponse(self._metadata.standardize)


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.delete = async_to_raw_response_wrapper(
            metadata.delete,
        )
        self.apply_standardization_db = async_to_raw_response_wrapper(
            metadata.apply_standardization_db,
        )
        self.count_distributions = async_to_raw_response_wrapper(
            metadata.count_distributions,
        )
        self.filter_by_conditions = async_to_raw_response_wrapper(
            metadata.filter_by_conditions,
        )
        self.get_basic_metadata = async_to_raw_response_wrapper(
            metadata.get_basic_metadata,
        )
        self.get_distinct_values = async_to_raw_response_wrapper(
            metadata.get_distinct_values,
        )
        self.get_distributions = async_to_raw_response_wrapper(
            metadata.get_distributions,
        )
        self.get_evidence = async_to_raw_response_wrapper(
            metadata.get_evidence,
        )
        self.get_filtered_metadata = async_to_raw_response_wrapper(
            metadata.get_filtered_metadata,
        )
        self.get_oob_tagged_file_count = async_to_raw_response_wrapper(
            metadata.get_oob_tagged_file_count,
        )
        self.get_tag_statistics = async_to_raw_response_wrapper(
            metadata.get_tag_statistics,
        )
        self.get_unique_tags = async_to_raw_response_wrapper(
            metadata.get_unique_tags,
        )
        self.suggest_standardization = async_to_raw_response_wrapper(
            metadata.suggest_standardization,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithRawResponse:
        return AsyncFileResourceWithRawResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> AsyncChunkResourceWithRawResponse:
        return AsyncChunkResourceWithRawResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> AsyncStandardizeResourceWithRawResponse:
        return AsyncStandardizeResourceWithRawResponse(self._metadata.standardize)


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.delete = to_streamed_response_wrapper(
            metadata.delete,
        )
        self.apply_standardization_db = to_streamed_response_wrapper(
            metadata.apply_standardization_db,
        )
        self.count_distributions = to_streamed_response_wrapper(
            metadata.count_distributions,
        )
        self.filter_by_conditions = to_streamed_response_wrapper(
            metadata.filter_by_conditions,
        )
        self.get_basic_metadata = to_streamed_response_wrapper(
            metadata.get_basic_metadata,
        )
        self.get_distinct_values = to_streamed_response_wrapper(
            metadata.get_distinct_values,
        )
        self.get_distributions = to_streamed_response_wrapper(
            metadata.get_distributions,
        )
        self.get_evidence = to_streamed_response_wrapper(
            metadata.get_evidence,
        )
        self.get_filtered_metadata = to_streamed_response_wrapper(
            metadata.get_filtered_metadata,
        )
        self.get_oob_tagged_file_count = to_streamed_response_wrapper(
            metadata.get_oob_tagged_file_count,
        )
        self.get_tag_statistics = to_streamed_response_wrapper(
            metadata.get_tag_statistics,
        )
        self.get_unique_tags = to_streamed_response_wrapper(
            metadata.get_unique_tags,
        )
        self.suggest_standardization = to_streamed_response_wrapper(
            metadata.suggest_standardization,
        )

    @cached_property
    def file(self) -> FileResourceWithStreamingResponse:
        return FileResourceWithStreamingResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> ChunkResourceWithStreamingResponse:
        return ChunkResourceWithStreamingResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> StandardizeResourceWithStreamingResponse:
        return StandardizeResourceWithStreamingResponse(self._metadata.standardize)


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.delete = async_to_streamed_response_wrapper(
            metadata.delete,
        )
        self.apply_standardization_db = async_to_streamed_response_wrapper(
            metadata.apply_standardization_db,
        )
        self.count_distributions = async_to_streamed_response_wrapper(
            metadata.count_distributions,
        )
        self.filter_by_conditions = async_to_streamed_response_wrapper(
            metadata.filter_by_conditions,
        )
        self.get_basic_metadata = async_to_streamed_response_wrapper(
            metadata.get_basic_metadata,
        )
        self.get_distinct_values = async_to_streamed_response_wrapper(
            metadata.get_distinct_values,
        )
        self.get_distributions = async_to_streamed_response_wrapper(
            metadata.get_distributions,
        )
        self.get_evidence = async_to_streamed_response_wrapper(
            metadata.get_evidence,
        )
        self.get_filtered_metadata = async_to_streamed_response_wrapper(
            metadata.get_filtered_metadata,
        )
        self.get_oob_tagged_file_count = async_to_streamed_response_wrapper(
            metadata.get_oob_tagged_file_count,
        )
        self.get_tag_statistics = async_to_streamed_response_wrapper(
            metadata.get_tag_statistics,
        )
        self.get_unique_tags = async_to_streamed_response_wrapper(
            metadata.get_unique_tags,
        )
        self.suggest_standardization = async_to_streamed_response_wrapper(
            metadata.suggest_standardization,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithStreamingResponse:
        return AsyncFileResourceWithStreamingResponse(self._metadata.file)

    @cached_property
    def chunk(self) -> AsyncChunkResourceWithStreamingResponse:
        return AsyncChunkResourceWithStreamingResponse(self._metadata.chunk)

    @cached_property
    def standardize(self) -> AsyncStandardizeResourceWithStreamingResponse:
        return AsyncStandardizeResourceWithStreamingResponse(self._metadata.standardize)
