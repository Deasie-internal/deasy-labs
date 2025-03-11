# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import (
    GraphListResponse,
    GraphDeleteResponse,
    GraphCreateOrUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraph:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DeasyLabs) -> None:
        graph = client.graph.list()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: DeasyLabs) -> None:
        graph = client.graph.list(
            graph_ids=["string"],
        )
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DeasyLabs) -> None:
        response = client.graph.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DeasyLabs) -> None:
        with client.graph.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphListResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DeasyLabs) -> None:
        graph = client.graph.delete(
            graph_id="graph_id",
        )
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DeasyLabs) -> None:
        response = client.graph.with_raw_response.delete(
            graph_id="graph_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DeasyLabs) -> None:
        with client.graph.with_streaming_response.delete(
            graph_id="graph_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphDeleteResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update(self, client: DeasyLabs) -> None:
        graph = client.graph.create_or_update()
        assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_or_update_with_all_params(self, client: DeasyLabs) -> None:
        graph = client.graph.create_or_update(
            graph_data={},
            graph_description="graph_description",
            graph_id="graph_id",
            graph_name="graph_name",
        )
        assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_or_update(self, client: DeasyLabs) -> None:
        response = client.graph.with_raw_response.create_or_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_or_update(self, client: DeasyLabs) -> None:
        with client.graph.with_streaming_response.create_or_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGraph:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasyLabs) -> None:
        graph = await async_client.graph.list()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        graph = await async_client.graph.list(
            graph_ids=["string"],
        )
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.graph.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphListResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.graph.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphListResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasyLabs) -> None:
        graph = await async_client.graph.delete(
            graph_id="graph_id",
        )
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.graph.with_raw_response.delete(
            graph_id="graph_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.graph.with_streaming_response.delete(
            graph_id="graph_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphDeleteResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncDeasyLabs) -> None:
        graph = await async_client.graph.create_or_update()
        assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        graph = await async_client.graph.create_or_update(
            graph_data={},
            graph_description="graph_description",
            graph_id="graph_id",
            graph_name="graph_name",
        )
        assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.graph.with_raw_response.create_or_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.graph.with_streaming_response.create_or_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphCreateOrUpdateResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True
