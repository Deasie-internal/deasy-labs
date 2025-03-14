# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.metadata import ChunkListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChunk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Deasy) -> None:
        chunk = client.metadata.chunk.list(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(ChunkListResponse, chunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Deasy) -> None:
        chunk = client.metadata.chunk.list(
            vector_db_config={},
            x_user="x-user",
            file_names=["string"],
            metadata_keys=["string"],
            search_query="search_query",
        )
        assert_matches_type(ChunkListResponse, chunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Deasy) -> None:
        response = client.metadata.chunk.with_raw_response.list(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = response.parse()
        assert_matches_type(ChunkListResponse, chunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Deasy) -> None:
        with client.metadata.chunk.with_streaming_response.list(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = response.parse()
            assert_matches_type(ChunkListResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChunk:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasy) -> None:
        chunk = await async_client.metadata.chunk.list(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(ChunkListResponse, chunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDeasy) -> None:
        chunk = await async_client.metadata.chunk.list(
            vector_db_config={},
            x_user="x-user",
            file_names=["string"],
            metadata_keys=["string"],
            search_query="search_query",
        )
        assert_matches_type(ChunkListResponse, chunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.chunk.with_raw_response.list(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chunk = await response.parse()
        assert_matches_type(ChunkListResponse, chunk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.chunk.with_streaming_response.list(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chunk = await response.parse()
            assert_matches_type(ChunkListResponse, chunk, path=["response"])

        assert cast(Any, response.is_closed) is True
