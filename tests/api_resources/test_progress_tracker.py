# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import (
    ProgressTrackerRetrieveTaskStatusResponse,
    ProgressTrackerListProgressTrackersResponse,
    ProgressTrackerDeleteProgressTrackersResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProgressTracker:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_abort_progress_tracker(self, client: Deasy) -> None:
        progress_tracker = client.progress_tracker.abort_progress_tracker(
            "tracker_id",
        )
        assert_matches_type(object, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_abort_progress_tracker(self, client: Deasy) -> None:
        response = client.progress_tracker.with_raw_response.abort_progress_tracker(
            "tracker_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = response.parse()
        assert_matches_type(object, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_abort_progress_tracker(self, client: Deasy) -> None:
        with client.progress_tracker.with_streaming_response.abort_progress_tracker(
            "tracker_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = response.parse()
            assert_matches_type(object, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_abort_progress_tracker(self, client: Deasy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracker_id` but received ''"):
            client.progress_tracker.with_raw_response.abort_progress_tracker(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_progress_trackers(self, client: Deasy) -> None:
        progress_tracker = client.progress_tracker.delete_progress_trackers(
            tracker_ids=["string"],
        )
        assert_matches_type(ProgressTrackerDeleteProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_progress_trackers(self, client: Deasy) -> None:
        response = client.progress_tracker.with_raw_response.delete_progress_trackers(
            tracker_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = response.parse()
        assert_matches_type(ProgressTrackerDeleteProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_progress_trackers(self, client: Deasy) -> None:
        with client.progress_tracker.with_streaming_response.delete_progress_trackers(
            tracker_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = response.parse()
            assert_matches_type(ProgressTrackerDeleteProgressTrackersResponse, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_progress_trackers(self, client: Deasy) -> None:
        progress_tracker = client.progress_tracker.list_progress_trackers()
        assert_matches_type(ProgressTrackerListProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_progress_trackers(self, client: Deasy) -> None:
        response = client.progress_tracker.with_raw_response.list_progress_trackers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = response.parse()
        assert_matches_type(ProgressTrackerListProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_progress_trackers(self, client: Deasy) -> None:
        with client.progress_tracker.with_streaming_response.list_progress_trackers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = response.parse()
            assert_matches_type(ProgressTrackerListProgressTrackersResponse, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_task_status(self, client: Deasy) -> None:
        progress_tracker = client.progress_tracker.retrieve_task_status(
            "job_id",
        )
        assert_matches_type(ProgressTrackerRetrieveTaskStatusResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_task_status(self, client: Deasy) -> None:
        response = client.progress_tracker.with_raw_response.retrieve_task_status(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = response.parse()
        assert_matches_type(ProgressTrackerRetrieveTaskStatusResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_task_status(self, client: Deasy) -> None:
        with client.progress_tracker.with_streaming_response.retrieve_task_status(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = response.parse()
            assert_matches_type(ProgressTrackerRetrieveTaskStatusResponse, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_task_status(self, client: Deasy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.progress_tracker.with_raw_response.retrieve_task_status(
                "",
            )


class TestAsyncProgressTracker:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_abort_progress_tracker(self, async_client: AsyncDeasy) -> None:
        progress_tracker = await async_client.progress_tracker.abort_progress_tracker(
            "tracker_id",
        )
        assert_matches_type(object, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_abort_progress_tracker(self, async_client: AsyncDeasy) -> None:
        response = await async_client.progress_tracker.with_raw_response.abort_progress_tracker(
            "tracker_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = await response.parse()
        assert_matches_type(object, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_abort_progress_tracker(self, async_client: AsyncDeasy) -> None:
        async with async_client.progress_tracker.with_streaming_response.abort_progress_tracker(
            "tracker_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = await response.parse()
            assert_matches_type(object, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_abort_progress_tracker(self, async_client: AsyncDeasy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracker_id` but received ''"):
            await async_client.progress_tracker.with_raw_response.abort_progress_tracker(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_progress_trackers(self, async_client: AsyncDeasy) -> None:
        progress_tracker = await async_client.progress_tracker.delete_progress_trackers(
            tracker_ids=["string"],
        )
        assert_matches_type(ProgressTrackerDeleteProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_progress_trackers(self, async_client: AsyncDeasy) -> None:
        response = await async_client.progress_tracker.with_raw_response.delete_progress_trackers(
            tracker_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = await response.parse()
        assert_matches_type(ProgressTrackerDeleteProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_progress_trackers(self, async_client: AsyncDeasy) -> None:
        async with async_client.progress_tracker.with_streaming_response.delete_progress_trackers(
            tracker_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = await response.parse()
            assert_matches_type(ProgressTrackerDeleteProgressTrackersResponse, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_progress_trackers(self, async_client: AsyncDeasy) -> None:
        progress_tracker = await async_client.progress_tracker.list_progress_trackers()
        assert_matches_type(ProgressTrackerListProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_progress_trackers(self, async_client: AsyncDeasy) -> None:
        response = await async_client.progress_tracker.with_raw_response.list_progress_trackers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = await response.parse()
        assert_matches_type(ProgressTrackerListProgressTrackersResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_progress_trackers(self, async_client: AsyncDeasy) -> None:
        async with async_client.progress_tracker.with_streaming_response.list_progress_trackers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = await response.parse()
            assert_matches_type(ProgressTrackerListProgressTrackersResponse, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_task_status(self, async_client: AsyncDeasy) -> None:
        progress_tracker = await async_client.progress_tracker.retrieve_task_status(
            "job_id",
        )
        assert_matches_type(ProgressTrackerRetrieveTaskStatusResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_task_status(self, async_client: AsyncDeasy) -> None:
        response = await async_client.progress_tracker.with_raw_response.retrieve_task_status(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        progress_tracker = await response.parse()
        assert_matches_type(ProgressTrackerRetrieveTaskStatusResponse, progress_tracker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_task_status(self, async_client: AsyncDeasy) -> None:
        async with async_client.progress_tracker.with_streaming_response.retrieve_task_status(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            progress_tracker = await response.parse()
            assert_matches_type(ProgressTrackerRetrieveTaskStatusResponse, progress_tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_task_status(self, async_client: AsyncDeasy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.progress_tracker.with_raw_response.retrieve_task_status(
                "",
            )
