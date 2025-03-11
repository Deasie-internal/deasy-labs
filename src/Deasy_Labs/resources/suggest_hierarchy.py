# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import suggest_hierarchy_suggest_params
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
from ..types.suggest_hierarchy_suggest_response import SuggestHierarchySuggestResponse

__all__ = ["SuggestHierarchyResource", "AsyncSuggestHierarchyResource"]


class SuggestHierarchyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SuggestHierarchyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return SuggestHierarchyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuggestHierarchyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return SuggestHierarchyResourceWithStreamingResponse(self)

    def suggest(
        self,
        *,
        condition: object,
        endpoint_manager_config: object,
        vector_db_config: object,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        context_level: Optional[str] | NotGiven = NOT_GIVEN,
        current_tree: Optional[object] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        max_height: Optional[int] | NotGiven = NOT_GIVEN,
        node: Optional[object] | NotGiven = NOT_GIVEN,
        tag_type: Optional[str] | NotGiven = NOT_GIVEN,
        total_files: Optional[int] | NotGiven = NOT_GIVEN,
        use_existing_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        use_extracted_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuggestHierarchySuggestResponse:
        """
        Suggest a hierarchical tag schema based on file content and existing metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/suggest_hierarchy",
            body=maybe_transform(
                {
                    "condition": condition,
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "context": context,
                    "context_level": context_level,
                    "current_tree": current_tree,
                    "file_names": file_names,
                    "max_height": max_height,
                    "node": node,
                    "tag_type": tag_type,
                    "total_files": total_files,
                    "use_existing_tags": use_existing_tags,
                    "use_extracted_tags": use_extracted_tags,
                    "usecase_id": usecase_id,
                },
                suggest_hierarchy_suggest_params.SuggestHierarchySuggestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuggestHierarchySuggestResponse,
        )


class AsyncSuggestHierarchyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSuggestHierarchyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuggestHierarchyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuggestHierarchyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncSuggestHierarchyResourceWithStreamingResponse(self)

    async def suggest(
        self,
        *,
        condition: object,
        endpoint_manager_config: object,
        vector_db_config: object,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        context_level: Optional[str] | NotGiven = NOT_GIVEN,
        current_tree: Optional[object] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        max_height: Optional[int] | NotGiven = NOT_GIVEN,
        node: Optional[object] | NotGiven = NOT_GIVEN,
        tag_type: Optional[str] | NotGiven = NOT_GIVEN,
        total_files: Optional[int] | NotGiven = NOT_GIVEN,
        use_existing_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        use_extracted_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuggestHierarchySuggestResponse:
        """
        Suggest a hierarchical tag schema based on file content and existing metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/suggest_hierarchy",
            body=await async_maybe_transform(
                {
                    "condition": condition,
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "context": context,
                    "context_level": context_level,
                    "current_tree": current_tree,
                    "file_names": file_names,
                    "max_height": max_height,
                    "node": node,
                    "tag_type": tag_type,
                    "total_files": total_files,
                    "use_existing_tags": use_existing_tags,
                    "use_extracted_tags": use_extracted_tags,
                    "usecase_id": usecase_id,
                },
                suggest_hierarchy_suggest_params.SuggestHierarchySuggestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuggestHierarchySuggestResponse,
        )


class SuggestHierarchyResourceWithRawResponse:
    def __init__(self, suggest_hierarchy: SuggestHierarchyResource) -> None:
        self._suggest_hierarchy = suggest_hierarchy

        self.suggest = to_raw_response_wrapper(
            suggest_hierarchy.suggest,
        )


class AsyncSuggestHierarchyResourceWithRawResponse:
    def __init__(self, suggest_hierarchy: AsyncSuggestHierarchyResource) -> None:
        self._suggest_hierarchy = suggest_hierarchy

        self.suggest = async_to_raw_response_wrapper(
            suggest_hierarchy.suggest,
        )


class SuggestHierarchyResourceWithStreamingResponse:
    def __init__(self, suggest_hierarchy: SuggestHierarchyResource) -> None:
        self._suggest_hierarchy = suggest_hierarchy

        self.suggest = to_streamed_response_wrapper(
            suggest_hierarchy.suggest,
        )


class AsyncSuggestHierarchyResourceWithStreamingResponse:
    def __init__(self, suggest_hierarchy: AsyncSuggestHierarchyResource) -> None:
        self._suggest_hierarchy = suggest_hierarchy

        self.suggest = async_to_streamed_response_wrapper(
            suggest_hierarchy.suggest,
        )
