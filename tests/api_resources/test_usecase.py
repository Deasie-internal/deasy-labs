# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import (
    UsecaseListResponse,
    UsecaseCreateResponse,
    UsecaseDeleteResponse,
    UsecaseGetFilesResponse,
    UsecaseCheckSyncResponse,
    UsecaseGetMetricsResponse,
    UsecaseGetFileCountResponse,
    UsecaseGetTagVdbDistributionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsecase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DeasyLabs) -> None:
        usecase = client.usecase.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DeasyLabs) -> None:
        usecase = client.usecase.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
            condition_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
        )
        assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DeasyLabs) -> None:
        usecase = client.usecase.list()
        assert_matches_type(UsecaseListResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseListResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseListResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DeasyLabs) -> None:
        usecase = client.usecase.delete(
            usecase_id="usecase_id",
        )
        assert_matches_type(UsecaseDeleteResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.delete(
            usecase_id="usecase_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseDeleteResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.delete(
            usecase_id="usecase_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseDeleteResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_check_sync(self, client: DeasyLabs) -> None:
        usecase = client.usecase.check_sync()
        assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_sync_with_all_params(self, client: DeasyLabs) -> None:
        usecase = client.usecase.check_sync(
            hard_limit=0,
            usecase_id="usecase_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_sync(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.check_sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_sync(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.check_sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_file_count(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_file_count(
            condition=[{}],
            vector_db_config={},
        )
        assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_file_count_with_all_params(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_file_count(
            condition=[{}],
            vector_db_config={},
            new_condition={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            usecase_id="usecase_id",
        )
        assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_file_count(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.get_file_count(
            condition=[{}],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_file_count(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.get_file_count(
            condition=[{}],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_files(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_files(
            usecase_id="usecase_id",
        )
        assert_matches_type(UsecaseGetFilesResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_files(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.get_files(
            usecase_id="usecase_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseGetFilesResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_files(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.get_files(
            usecase_id="usecase_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseGetFilesResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_metrics(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_metrics()
        assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_metrics_with_all_params(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_metrics(
            file_names=["string"],
            node_ids=["string"],
            tags=["string"],
            usecase_id="usecase_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_metrics(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.get_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_metrics(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.get_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_tag_vdb_distribution(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_tag_vdb_distribution()
        assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_tag_vdb_distribution_with_all_params(self, client: DeasyLabs) -> None:
        usecase = client.usecase.get_tag_vdb_distribution(
            usecase_id="usecase_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_tag_vdb_distribution(self, client: DeasyLabs) -> None:
        response = client.usecase.with_raw_response.get_tag_vdb_distribution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_tag_vdb_distribution(self, client: DeasyLabs) -> None:
        with client.usecase.with_streaming_response.get_tag_vdb_distribution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsecase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
            condition_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
        )
        assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.create(
            condition=[{}],
            data_points=0,
            description="description",
            graph_id="graph_id",
            last_updated="last_updated",
            latest_graph={},
            status="status",
            usecase_id="usecase_id",
            usecase_name="usecase_name",
            user_id="user_id",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseCreateResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.list()
        assert_matches_type(UsecaseListResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseListResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseListResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.delete(
            usecase_id="usecase_id",
        )
        assert_matches_type(UsecaseDeleteResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.delete(
            usecase_id="usecase_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseDeleteResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.delete(
            usecase_id="usecase_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseDeleteResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_sync(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.check_sync()
        assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_sync_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.check_sync(
            hard_limit=0,
            usecase_id="usecase_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_sync(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.check_sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_sync(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.check_sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseCheckSyncResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_file_count(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_file_count(
            condition=[{}],
            vector_db_config={},
        )
        assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_file_count_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_file_count(
            condition=[{}],
            vector_db_config={},
            new_condition={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            usecase_id="usecase_id",
        )
        assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_file_count(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.get_file_count(
            condition=[{}],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_file_count(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.get_file_count(
            condition=[{}],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseGetFileCountResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_files(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_files(
            usecase_id="usecase_id",
        )
        assert_matches_type(UsecaseGetFilesResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_files(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.get_files(
            usecase_id="usecase_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseGetFilesResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_files(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.get_files(
            usecase_id="usecase_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseGetFilesResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_metrics(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_metrics()
        assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_metrics_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_metrics(
            file_names=["string"],
            node_ids=["string"],
            tags=["string"],
            usecase_id="usecase_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_metrics(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.get_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_metrics(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.get_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseGetMetricsResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_tag_vdb_distribution(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_tag_vdb_distribution()
        assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_tag_vdb_distribution_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        usecase = await async_client.usecase.get_tag_vdb_distribution(
            usecase_id="usecase_id",
            vector_db_config={},
        )
        assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_tag_vdb_distribution(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.with_raw_response.get_tag_vdb_distribution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_tag_vdb_distribution(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.with_streaming_response.get_tag_vdb_distribution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseGetTagVdbDistributionResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True
