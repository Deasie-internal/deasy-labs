# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import classify_classify_files_params
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
from ..types.classify_classify_files_response import ClassifyClassifyFilesResponse

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def classify_files(
        self,
        *,
        dataslice_id: Optional[str],
        file_names: Optional[List[str]],
        hierarchy_name: Optional[str],
        llm_profile_name: Optional[str],
        tag_datas: Optional[Dict[str, classify_classify_files_params.TagDatas]],
        tag_names: Optional[List[str]],
        vdb_profile_name: str,
        hierarchy_data: Optional[object] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        soft_run: bool | NotGiven = NOT_GIVEN,
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
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "hierarchy_name": hierarchy_name,
                    "llm_profile_name": llm_profile_name,
                    "tag_datas": tag_datas,
                    "tag_names": tag_names,
                    "vdb_profile_name": vdb_profile_name,
                    "hierarchy_data": hierarchy_data,
                    "job_id": job_id,
                    "overwrite": overwrite,
                    "soft_run": soft_run,
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

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-python#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def classify_files(
        self,
        *,
        dataslice_id: Optional[str],
        file_names: Optional[List[str]],
        hierarchy_name: Optional[str],
        llm_profile_name: Optional[str],
        tag_datas: Optional[Dict[str, classify_classify_files_params.TagDatas]],
        tag_names: Optional[List[str]],
        vdb_profile_name: str,
        hierarchy_data: Optional[object] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        soft_run: bool | NotGiven = NOT_GIVEN,
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
                    "dataslice_id": dataslice_id,
                    "file_names": file_names,
                    "hierarchy_name": hierarchy_name,
                    "llm_profile_name": llm_profile_name,
                    "tag_datas": tag_datas,
                    "tag_names": tag_names,
                    "vdb_profile_name": vdb_profile_name,
                    "hierarchy_data": hierarchy_data,
                    "job_id": job_id,
                    "overwrite": overwrite,
                    "soft_run": soft_run,
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

        self.classify_files = to_raw_response_wrapper(
            classify.classify_files,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.classify_files = async_to_raw_response_wrapper(
            classify.classify_files,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.classify_files = to_streamed_response_wrapper(
            classify.classify_files,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.classify_files = async_to_streamed_response_wrapper(
            classify.classify_files,
        )
