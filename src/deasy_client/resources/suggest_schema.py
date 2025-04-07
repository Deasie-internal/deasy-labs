# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ..types import suggest_schema_create_params
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
from ..types.condition_input_param import ConditionInputParam
from ..types.suggest_schema_create_response import SuggestSchemaCreateResponse

__all__ = ["SuggestSchemaResource", "AsyncSuggestSchemaResource"]


class SuggestSchemaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SuggestSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#accessing-raw-response-data-eg-headers
        """
        return SuggestSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuggestSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#with_streaming_response
        """
        return SuggestSchemaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        vdb_profile_name: str,
        condition: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        context_level: Optional[str] | NotGiven = NOT_GIVEN,
        current_tree: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        graph_tag_type: Optional[Literal["open_ended", "binary", "mixed", "defined_values"]] | NotGiven = NOT_GIVEN,
        llm_profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        max_height: Optional[int] | NotGiven = NOT_GIVEN,
        max_tags_per_level: Optional[int] | NotGiven = NOT_GIVEN,
        min_tags_per_level: Optional[int] | NotGiven = NOT_GIVEN,
        node: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        use_existing_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        use_extracted_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        user_context: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuggestSchemaCreateResponse:
        """
        Suggest a hierarchical tag schema based on file content and existing metadata

        Attributes:

            vdb_profile_name: The name of the vector database profile to use for accessing file content.
            llm_profile_name: Optional name of the language model profile to use for generating suggestions. Defaults to DeasyLabs compute
            file_names: Optional list of specific files to analyze for the hierarchy suggestion.
            dataslice_id: Optional ID of a dataslice to pull files from for the hierarchy suggestion.
            current_tree: Optional existing hierarchy tree to build upon.
            node: Optional node location of the existing hierarchy tree to build upon.
            condition: Optional filtering condition to select specific files for analysis.
            user_context: Optional user-provided context to guide the suggestion process.
            context_level: Level at which to analyze content ('file' or 'chunk'). Defaults to 'file'.
            max_height: Maximum depth of the generated hierarchy tree. Defaults to 2.
            use_existing_tags: Whether to incorporate existing tags in suggestions. Defaults to False.
            use_extracted_tags: Whether to use previously extracted tags. Defaults to False.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/suggest_schema",
            body=maybe_transform(
                {
                    "vdb_profile_name": vdb_profile_name,
                    "condition": condition,
                    "context_level": context_level,
                    "current_tree": current_tree,
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "graph_tag_type": graph_tag_type,
                    "llm_profile_name": llm_profile_name,
                    "max_height": max_height,
                    "max_tags_per_level": max_tags_per_level,
                    "min_tags_per_level": min_tags_per_level,
                    "node": node,
                    "use_existing_tags": use_existing_tags,
                    "use_extracted_tags": use_extracted_tags,
                    "user_context": user_context,
                },
                suggest_schema_create_params.SuggestSchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuggestSchemaCreateResponse,
        )


class AsyncSuggestSchemaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSuggestSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#accessing-raw-response-data-eg-headers
        """
        return AsyncSuggestSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuggestSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-labs#with_streaming_response
        """
        return AsyncSuggestSchemaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        vdb_profile_name: str,
        condition: Optional[ConditionInputParam] | NotGiven = NOT_GIVEN,
        context_level: Optional[str] | NotGiven = NOT_GIVEN,
        current_tree: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        graph_tag_type: Optional[Literal["open_ended", "binary", "mixed", "defined_values"]] | NotGiven = NOT_GIVEN,
        llm_profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        max_height: Optional[int] | NotGiven = NOT_GIVEN,
        max_tags_per_level: Optional[int] | NotGiven = NOT_GIVEN,
        min_tags_per_level: Optional[int] | NotGiven = NOT_GIVEN,
        node: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        use_existing_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        use_extracted_tags: Optional[bool] | NotGiven = NOT_GIVEN,
        user_context: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuggestSchemaCreateResponse:
        """
        Suggest a hierarchical tag schema based on file content and existing metadata

        Attributes:

            vdb_profile_name: The name of the vector database profile to use for accessing file content.
            llm_profile_name: Optional name of the language model profile to use for generating suggestions. Defaults to DeasyLabs compute
            file_names: Optional list of specific files to analyze for the hierarchy suggestion.
            dataslice_id: Optional ID of a dataslice to pull files from for the hierarchy suggestion.
            current_tree: Optional existing hierarchy tree to build upon.
            node: Optional node location of the existing hierarchy tree to build upon.
            condition: Optional filtering condition to select specific files for analysis.
            user_context: Optional user-provided context to guide the suggestion process.
            context_level: Level at which to analyze content ('file' or 'chunk'). Defaults to 'file'.
            max_height: Maximum depth of the generated hierarchy tree. Defaults to 2.
            use_existing_tags: Whether to incorporate existing tags in suggestions. Defaults to False.
            use_extracted_tags: Whether to use previously extracted tags. Defaults to False.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/suggest_schema",
            body=await async_maybe_transform(
                {
                    "vdb_profile_name": vdb_profile_name,
                    "condition": condition,
                    "context_level": context_level,
                    "current_tree": current_tree,
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "graph_tag_type": graph_tag_type,
                    "llm_profile_name": llm_profile_name,
                    "max_height": max_height,
                    "max_tags_per_level": max_tags_per_level,
                    "min_tags_per_level": min_tags_per_level,
                    "node": node,
                    "use_existing_tags": use_existing_tags,
                    "use_extracted_tags": use_extracted_tags,
                    "user_context": user_context,
                },
                suggest_schema_create_params.SuggestSchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuggestSchemaCreateResponse,
        )


class SuggestSchemaResourceWithRawResponse:
    def __init__(self, suggest_schema: SuggestSchemaResource) -> None:
        self._suggest_schema = suggest_schema

        self.create = to_raw_response_wrapper(
            suggest_schema.create,
        )


class AsyncSuggestSchemaResourceWithRawResponse:
    def __init__(self, suggest_schema: AsyncSuggestSchemaResource) -> None:
        self._suggest_schema = suggest_schema

        self.create = async_to_raw_response_wrapper(
            suggest_schema.create,
        )


class SuggestSchemaResourceWithStreamingResponse:
    def __init__(self, suggest_schema: SuggestSchemaResource) -> None:
        self._suggest_schema = suggest_schema

        self.create = to_streamed_response_wrapper(
            suggest_schema.create,
        )


class AsyncSuggestSchemaResourceWithStreamingResponse:
    def __init__(self, suggest_schema: AsyncSuggestSchemaResource) -> None:
        self._suggest_schema = suggest_schema

        self.create = async_to_streamed_response_wrapper(
            suggest_schema.create,
        )
