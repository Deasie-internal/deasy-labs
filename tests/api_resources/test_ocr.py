# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOcr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ingest(self, client: Deasy) -> None:
        ocr = client.ocr.ingest(
            data_source_manager_config={},
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ingest_with_all_params(self, client: Deasy) -> None:
        ocr = client.ocr.ingest(
            data_source_manager_config={},
            clean_up_out_of_sync=True,
            endpoint_manager_config={},
            file_count_to_run=0,
            file_names=["string"],
            job_id="job_id",
            use_llm=True,
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ingest(self, client: Deasy) -> None:
        response = client.ocr.with_raw_response.ingest(
            data_source_manager_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ocr = response.parse()
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ingest(self, client: Deasy) -> None:
        with client.ocr.with_streaming_response.ingest(
            data_source_manager_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ocr = response.parse()
            assert_matches_type(object, ocr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_sync_stats(self, client: Deasy) -> None:
        ocr = client.ocr.sync_stats(
            data_source_manager_configs=[{}],
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_sync_stats_with_all_params(self, client: Deasy) -> None:
        ocr = client.ocr.sync_stats(
            data_source_manager_configs=[{}],
            use_cache=True,
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_sync_stats(self, client: Deasy) -> None:
        response = client.ocr.with_raw_response.sync_stats(
            data_source_manager_configs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ocr = response.parse()
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_sync_stats(self, client: Deasy) -> None:
        with client.ocr.with_streaming_response.sync_stats(
            data_source_manager_configs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ocr = response.parse()
            assert_matches_type(object, ocr, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOcr:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ingest(self, async_client: AsyncDeasy) -> None:
        ocr = await async_client.ocr.ingest(
            data_source_manager_config={},
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ingest_with_all_params(self, async_client: AsyncDeasy) -> None:
        ocr = await async_client.ocr.ingest(
            data_source_manager_config={},
            clean_up_out_of_sync=True,
            endpoint_manager_config={},
            file_count_to_run=0,
            file_names=["string"],
            job_id="job_id",
            use_llm=True,
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncDeasy) -> None:
        response = await async_client.ocr.with_raw_response.ingest(
            data_source_manager_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ocr = await response.parse()
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncDeasy) -> None:
        async with async_client.ocr.with_streaming_response.ingest(
            data_source_manager_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ocr = await response.parse()
            assert_matches_type(object, ocr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_sync_stats(self, async_client: AsyncDeasy) -> None:
        ocr = await async_client.ocr.sync_stats(
            data_source_manager_configs=[{}],
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_sync_stats_with_all_params(self, async_client: AsyncDeasy) -> None:
        ocr = await async_client.ocr.sync_stats(
            data_source_manager_configs=[{}],
            use_cache=True,
        )
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_sync_stats(self, async_client: AsyncDeasy) -> None:
        response = await async_client.ocr.with_raw_response.sync_stats(
            data_source_manager_configs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ocr = await response.parse()
        assert_matches_type(object, ocr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_sync_stats(self, async_client: AsyncDeasy) -> None:
        async with async_client.ocr.with_streaming_response.sync_stats(
            data_source_manager_configs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ocr = await response.parse()
            assert_matches_type(object, ocr, path=["response"])

        assert cast(Any, response.is_closed) is True
