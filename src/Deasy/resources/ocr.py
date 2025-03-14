# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import ocr_ingest_params, ocr_sync_stats_params
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

__all__ = ["OcrResource", "AsyncOcrResource"]


class OcrResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OcrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return OcrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OcrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return OcrResourceWithStreamingResponse(self)

    def ingest(
        self,
        *,
        data_source_manager_config: object,
        clean_up_out_of_sync: bool | NotGiven = NOT_GIVEN,
        endpoint_manager_config: Optional[object] | NotGiven = NOT_GIVEN,
        file_count_to_run: Optional[int] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        use_llm: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Ingest OCR data into the vector database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ocr/ingest",
            body=maybe_transform(
                {
                    "data_source_manager_config": data_source_manager_config,
                    "clean_up_out_of_sync": clean_up_out_of_sync,
                    "endpoint_manager_config": endpoint_manager_config,
                    "file_count_to_run": file_count_to_run,
                    "file_names": file_names,
                    "job_id": job_id,
                    "use_llm": use_llm,
                },
                ocr_ingest_params.OcrIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def sync_stats(
        self,
        *,
        data_source_manager_configs: Iterable[object],
        use_cache: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get OCR sync statistics for multiple data sources, using cache with background
        refresh.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ocr/sync_stats",
            body=maybe_transform(
                {
                    "data_source_manager_configs": data_source_manager_configs,
                    "use_cache": use_cache,
                },
                ocr_sync_stats_params.OcrSyncStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOcrResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOcrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOcrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOcrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncOcrResourceWithStreamingResponse(self)

    async def ingest(
        self,
        *,
        data_source_manager_config: object,
        clean_up_out_of_sync: bool | NotGiven = NOT_GIVEN,
        endpoint_manager_config: Optional[object] | NotGiven = NOT_GIVEN,
        file_count_to_run: Optional[int] | NotGiven = NOT_GIVEN,
        file_names: Optional[List[str]] | NotGiven = NOT_GIVEN,
        job_id: Optional[str] | NotGiven = NOT_GIVEN,
        use_llm: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Ingest OCR data into the vector database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ocr/ingest",
            body=await async_maybe_transform(
                {
                    "data_source_manager_config": data_source_manager_config,
                    "clean_up_out_of_sync": clean_up_out_of_sync,
                    "endpoint_manager_config": endpoint_manager_config,
                    "file_count_to_run": file_count_to_run,
                    "file_names": file_names,
                    "job_id": job_id,
                    "use_llm": use_llm,
                },
                ocr_ingest_params.OcrIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def sync_stats(
        self,
        *,
        data_source_manager_configs: Iterable[object],
        use_cache: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get OCR sync statistics for multiple data sources, using cache with background
        refresh.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ocr/sync_stats",
            body=await async_maybe_transform(
                {
                    "data_source_manager_configs": data_source_manager_configs,
                    "use_cache": use_cache,
                },
                ocr_sync_stats_params.OcrSyncStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OcrResourceWithRawResponse:
    def __init__(self, ocr: OcrResource) -> None:
        self._ocr = ocr

        self.ingest = to_raw_response_wrapper(
            ocr.ingest,
        )
        self.sync_stats = to_raw_response_wrapper(
            ocr.sync_stats,
        )


class AsyncOcrResourceWithRawResponse:
    def __init__(self, ocr: AsyncOcrResource) -> None:
        self._ocr = ocr

        self.ingest = async_to_raw_response_wrapper(
            ocr.ingest,
        )
        self.sync_stats = async_to_raw_response_wrapper(
            ocr.sync_stats,
        )


class OcrResourceWithStreamingResponse:
    def __init__(self, ocr: OcrResource) -> None:
        self._ocr = ocr

        self.ingest = to_streamed_response_wrapper(
            ocr.ingest,
        )
        self.sync_stats = to_streamed_response_wrapper(
            ocr.sync_stats,
        )


class AsyncOcrResourceWithStreamingResponse:
    def __init__(self, ocr: AsyncOcrResource) -> None:
        self._ocr = ocr

        self.ingest = async_to_streamed_response_wrapper(
            ocr.ingest,
        )
        self.sync_stats = async_to_streamed_response_wrapper(
            ocr.sync_stats,
        )
