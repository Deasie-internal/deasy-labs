# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import progress_tracker_delete_progress_trackers_params
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
from ..types.progress_tracker_retrieve_task_status_response import ProgressTrackerRetrieveTaskStatusResponse
from ..types.progress_tracker_list_progress_trackers_response import ProgressTrackerListProgressTrackersResponse
from ..types.progress_tracker_delete_progress_trackers_response import ProgressTrackerDeleteProgressTrackersResponse

__all__ = ["ProgressTrackerResource", "AsyncProgressTrackerResource"]


class ProgressTrackerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProgressTrackerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return ProgressTrackerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProgressTrackerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return ProgressTrackerResourceWithStreamingResponse(self)

    def abort_progress_tracker(
        self,
        tracker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Abort a progress tracker and update the tracker in Postgres.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tracker_id:
            raise ValueError(f"Expected a non-empty value for `tracker_id` but received {tracker_id!r}")
        return self._put(
            f"/progress_tracker/abort_progress_tracker/{tracker_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete_progress_trackers(
        self,
        *,
        tracker_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProgressTrackerDeleteProgressTrackersResponse:
        """
        Delete a progress tracker from Postgres.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/progress_tracker/delete_progress_trackers",
            body=maybe_transform(
                {"tracker_ids": tracker_ids},
                progress_tracker_delete_progress_trackers_params.ProgressTrackerDeleteProgressTrackersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgressTrackerDeleteProgressTrackersResponse,
        )

    def list_progress_trackers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProgressTrackerListProgressTrackersResponse:
        """Get all progress trackers for a user."""
        return self._get(
            "/progress_tracker/get_progress_trackers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgressTrackerListProgressTrackersResponse,
        )

    def retrieve_task_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProgressTrackerRetrieveTaskStatusResponse:
        """
        Get Task Progress

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/progress_tracker/task_status/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgressTrackerRetrieveTaskStatusResponse,
        )


class AsyncProgressTrackerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProgressTrackerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProgressTrackerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProgressTrackerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncProgressTrackerResourceWithStreamingResponse(self)

    async def abort_progress_tracker(
        self,
        tracker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Abort a progress tracker and update the tracker in Postgres.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tracker_id:
            raise ValueError(f"Expected a non-empty value for `tracker_id` but received {tracker_id!r}")
        return await self._put(
            f"/progress_tracker/abort_progress_tracker/{tracker_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete_progress_trackers(
        self,
        *,
        tracker_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProgressTrackerDeleteProgressTrackersResponse:
        """
        Delete a progress tracker from Postgres.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/progress_tracker/delete_progress_trackers",
            body=await async_maybe_transform(
                {"tracker_ids": tracker_ids},
                progress_tracker_delete_progress_trackers_params.ProgressTrackerDeleteProgressTrackersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgressTrackerDeleteProgressTrackersResponse,
        )

    async def list_progress_trackers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProgressTrackerListProgressTrackersResponse:
        """Get all progress trackers for a user."""
        return await self._get(
            "/progress_tracker/get_progress_trackers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgressTrackerListProgressTrackersResponse,
        )

    async def retrieve_task_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProgressTrackerRetrieveTaskStatusResponse:
        """
        Get Task Progress

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/progress_tracker/task_status/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgressTrackerRetrieveTaskStatusResponse,
        )


class ProgressTrackerResourceWithRawResponse:
    def __init__(self, progress_tracker: ProgressTrackerResource) -> None:
        self._progress_tracker = progress_tracker

        self.abort_progress_tracker = to_raw_response_wrapper(
            progress_tracker.abort_progress_tracker,
        )
        self.delete_progress_trackers = to_raw_response_wrapper(
            progress_tracker.delete_progress_trackers,
        )
        self.list_progress_trackers = to_raw_response_wrapper(
            progress_tracker.list_progress_trackers,
        )
        self.retrieve_task_status = to_raw_response_wrapper(
            progress_tracker.retrieve_task_status,
        )


class AsyncProgressTrackerResourceWithRawResponse:
    def __init__(self, progress_tracker: AsyncProgressTrackerResource) -> None:
        self._progress_tracker = progress_tracker

        self.abort_progress_tracker = async_to_raw_response_wrapper(
            progress_tracker.abort_progress_tracker,
        )
        self.delete_progress_trackers = async_to_raw_response_wrapper(
            progress_tracker.delete_progress_trackers,
        )
        self.list_progress_trackers = async_to_raw_response_wrapper(
            progress_tracker.list_progress_trackers,
        )
        self.retrieve_task_status = async_to_raw_response_wrapper(
            progress_tracker.retrieve_task_status,
        )


class ProgressTrackerResourceWithStreamingResponse:
    def __init__(self, progress_tracker: ProgressTrackerResource) -> None:
        self._progress_tracker = progress_tracker

        self.abort_progress_tracker = to_streamed_response_wrapper(
            progress_tracker.abort_progress_tracker,
        )
        self.delete_progress_trackers = to_streamed_response_wrapper(
            progress_tracker.delete_progress_trackers,
        )
        self.list_progress_trackers = to_streamed_response_wrapper(
            progress_tracker.list_progress_trackers,
        )
        self.retrieve_task_status = to_streamed_response_wrapper(
            progress_tracker.retrieve_task_status,
        )


class AsyncProgressTrackerResourceWithStreamingResponse:
    def __init__(self, progress_tracker: AsyncProgressTrackerResource) -> None:
        self._progress_tracker = progress_tracker

        self.abort_progress_tracker = async_to_streamed_response_wrapper(
            progress_tracker.abort_progress_tracker,
        )
        self.delete_progress_trackers = async_to_streamed_response_wrapper(
            progress_tracker.delete_progress_trackers,
        )
        self.list_progress_trackers = async_to_streamed_response_wrapper(
            progress_tracker.list_progress_trackers,
        )
        self.retrieve_task_status = async_to_streamed_response_wrapper(
            progress_tracker.retrieve_task_status,
        )
