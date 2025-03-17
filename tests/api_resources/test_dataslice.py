# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import (
    DatasliceListResponse,
    DatasliceCreateResponse,
    DatasliceDeleteResponse,
    DatasliceGetFilesResponse,
    DatasliceTagVdbDistributionResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataslice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Deasy) -> None:
        dataslice = client.dataslice.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Deasy) -> None:
        dataslice = client.dataslice.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
            condition=[{}],
            condition_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            data_points=0,
            description="description",
            status="status",
        )
        assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Deasy) -> None:
        response = client.dataslice.with_raw_response.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = response.parse()
        assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Deasy) -> None:
        with client.dataslice.with_streaming_response.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = response.parse()
            assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Deasy) -> None:
        dataslice = client.dataslice.list()
        assert_matches_type(DatasliceListResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Deasy) -> None:
        response = client.dataslice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = response.parse()
        assert_matches_type(DatasliceListResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Deasy) -> None:
        with client.dataslice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = response.parse()
            assert_matches_type(DatasliceListResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        dataslice = client.dataslice.delete(
            dataslice_id="dataslice_id",
        )
        assert_matches_type(DatasliceDeleteResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.dataslice.with_raw_response.delete(
            dataslice_id="dataslice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = response.parse()
        assert_matches_type(DatasliceDeleteResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.dataslice.with_streaming_response.delete(
            dataslice_id="dataslice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = response.parse()
            assert_matches_type(DatasliceDeleteResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_files(self, client: Deasy) -> None:
        dataslice = client.dataslice.get_files(
            dataslice_id="dataslice_id",
        )
        assert_matches_type(DatasliceGetFilesResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_files(self, client: Deasy) -> None:
        response = client.dataslice.with_raw_response.get_files(
            dataslice_id="dataslice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = response.parse()
        assert_matches_type(DatasliceGetFilesResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_files(self, client: Deasy) -> None:
        with client.dataslice.with_streaming_response.get_files(
            dataslice_id="dataslice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = response.parse()
            assert_matches_type(DatasliceGetFilesResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_tag_vdb_distribution(self, client: Deasy) -> None:
        dataslice = client.dataslice.tag_vdb_distribution()
        assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tag_vdb_distribution_with_all_params(self, client: Deasy) -> None:
        dataslice = client.dataslice.tag_vdb_distribution(
            dataslice_id="dataslice_id",
            vector_db_config={},
        )
        assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tag_vdb_distribution(self, client: Deasy) -> None:
        response = client.dataslice.with_raw_response.tag_vdb_distribution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = response.parse()
        assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tag_vdb_distribution(self, client: Deasy) -> None:
        with client.dataslice.with_streaming_response.tag_vdb_distribution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = response.parse()
            assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataslice:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
            condition=[{}],
            condition_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            data_points=0,
            description="description",
            status="status",
        )
        assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasy) -> None:
        response = await async_client.dataslice.with_raw_response.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = await response.parse()
        assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasy) -> None:
        async with async_client.dataslice.with_streaming_response.create(
            dataslice_name="dataslice_name",
            graph_id="graph_id",
            latest_graph={},
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = await response.parse()
            assert_matches_type(DatasliceCreateResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.list()
        assert_matches_type(DatasliceListResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasy) -> None:
        response = await async_client.dataslice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = await response.parse()
        assert_matches_type(DatasliceListResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasy) -> None:
        async with async_client.dataslice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = await response.parse()
            assert_matches_type(DatasliceListResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.delete(
            dataslice_id="dataslice_id",
        )
        assert_matches_type(DatasliceDeleteResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.dataslice.with_raw_response.delete(
            dataslice_id="dataslice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = await response.parse()
        assert_matches_type(DatasliceDeleteResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.dataslice.with_streaming_response.delete(
            dataslice_id="dataslice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = await response.parse()
            assert_matches_type(DatasliceDeleteResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_files(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.get_files(
            dataslice_id="dataslice_id",
        )
        assert_matches_type(DatasliceGetFilesResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_files(self, async_client: AsyncDeasy) -> None:
        response = await async_client.dataslice.with_raw_response.get_files(
            dataslice_id="dataslice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = await response.parse()
        assert_matches_type(DatasliceGetFilesResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_files(self, async_client: AsyncDeasy) -> None:
        async with async_client.dataslice.with_streaming_response.get_files(
            dataslice_id="dataslice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = await response.parse()
            assert_matches_type(DatasliceGetFilesResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_tag_vdb_distribution(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.tag_vdb_distribution()
        assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tag_vdb_distribution_with_all_params(self, async_client: AsyncDeasy) -> None:
        dataslice = await async_client.dataslice.tag_vdb_distribution(
            dataslice_id="dataslice_id",
            vector_db_config={},
        )
        assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tag_vdb_distribution(self, async_client: AsyncDeasy) -> None:
        response = await async_client.dataslice.with_raw_response.tag_vdb_distribution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataslice = await response.parse()
        assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tag_vdb_distribution(self, async_client: AsyncDeasy) -> None:
        async with async_client.dataslice.with_streaming_response.tag_vdb_distribution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataslice = await response.parse()
            assert_matches_type(DatasliceTagVdbDistributionResponse, dataslice, path=["response"])

        assert cast(Any, response.is_closed) is True
