# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

from ..types import classify_classify_all_params, classify_classify_files_params
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
from ..types.classify_classify_all_response import ClassifyClassifyAllResponse
from ..types.classify_classify_files_response import ClassifyClassifyFilesResponse

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def classify_all(
        self,
        *,
        endpoint_manager_config: object,
        vector_db_config: object,
        conditions: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_file_tags: bool | NotGiven = NOT_GIVEN,
        hierarchy: Optional[object] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        llm_dry_run: bool | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        soft_run: bool | NotGiven = NOT_GIVEN,
        tags: Optional[Dict[str, classify_classify_all_params.Tags]] | NotGiven = NOT_GIVEN,
        total_data_sets: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyClassifyAllResponse:
        """
        Classify all files in data source in batches with the provided tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/classify/all",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "generate_file_tags": generate_file_tags,
                    "hierarchy": hierarchy,
                    "job_id": job_id,
                    "llm_dry_run": llm_dry_run,
                    "overwrite": overwrite,
                    "soft_run": soft_run,
                    "tags": tags,
                    "total_data_sets": total_data_sets,
                },
                classify_classify_all_params.ClassifyClassifyAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyClassifyAllResponse,
        )

    def classify_files(
        self,
        *,
        endpoint_manager_config: object,
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        generate_file_tags: bool | NotGiven = NOT_GIVEN,
        hierarchy: Optional[object] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        soft_run: bool | NotGiven = NOT_GIVEN,
        tags: Optional[Dict[str, classify_classify_files_params.Tags]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyClassifyFilesResponse:
        """
        Classify files specified in the request with the provided tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/classify",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "generate_file_tags": generate_file_tags,
                    "hierarchy": hierarchy,
                    "job_id": job_id,
                    "overwrite": overwrite,
                    "soft_run": soft_run,
                    "tags": tags,
                },
                classify_classify_files_params.ClassifyClassifyFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyClassifyFilesResponse,
        )


class AsyncClassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def classify_all(
        self,
        *,
        endpoint_manager_config: object,
        vector_db_config: object,
        conditions: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        generate_file_tags: bool | NotGiven = NOT_GIVEN,
        hierarchy: Optional[object] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        llm_dry_run: bool | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        soft_run: bool | NotGiven = NOT_GIVEN,
        tags: Optional[Dict[str, classify_classify_all_params.Tags]] | NotGiven = NOT_GIVEN,
        total_data_sets: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyClassifyAllResponse:
        """
        Classify all files in data source in batches with the provided tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/classify/all",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "conditions": conditions,
                    "dataslice_id": dataslice_id,
                    "generate_file_tags": generate_file_tags,
                    "hierarchy": hierarchy,
                    "job_id": job_id,
                    "llm_dry_run": llm_dry_run,
                    "overwrite": overwrite,
                    "soft_run": soft_run,
                    "tags": tags,
                    "total_data_sets": total_data_sets,
                },
                classify_classify_all_params.ClassifyClassifyAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyClassifyAllResponse,
        )

    async def classify_files(
        self,
        *,
        endpoint_manager_config: object,
        vector_db_config: object,
        dataslice_id: Optional[str] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        generate_file_tags: bool | NotGiven = NOT_GIVEN,
        hierarchy: Optional[object] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        soft_run: bool | NotGiven = NOT_GIVEN,
        tags: Optional[Dict[str, classify_classify_files_params.Tags]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassifyClassifyFilesResponse:
        """
        Classify files specified in the request with the provided tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/classify",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "vector_db_config": vector_db_config,
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "generate_file_tags": generate_file_tags,
                    "hierarchy": hierarchy,
                    "job_id": job_id,
                    "overwrite": overwrite,
                    "soft_run": soft_run,
                    "tags": tags,
                },
                classify_classify_files_params.ClassifyClassifyFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyClassifyFilesResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.classify_all = to_raw_response_wrapper(
            classify.classify_all,
        )
        self.classify_files = to_raw_response_wrapper(
            classify.classify_files,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.classify_all = async_to_raw_response_wrapper(
            classify.classify_all,
        )
        self.classify_files = async_to_raw_response_wrapper(
            classify.classify_files,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.classify_all = to_streamed_response_wrapper(
            classify.classify_all,
        )
        self.classify_files = to_streamed_response_wrapper(
            classify.classify_files,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.classify_all = async_to_streamed_response_wrapper(
            classify.classify_all,
        )
        self.classify_files = async_to_streamed_response_wrapper(
            classify.classify_files,
        )
