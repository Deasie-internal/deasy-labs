# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.console import (
    VdbconnectorCreateResponse,
    VdbconnectorDeleteResponse,
    VdbconnectorGetDeleteStatsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVdbconnector:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Deasy) -> None:
        vdbconnector = client.console.vdbconnector.create(
            secret_name="secret_name",
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(VdbconnectorCreateResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Deasy) -> None:
        response = client.console.vdbconnector.with_raw_response.create(
            secret_name="secret_name",
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vdbconnector = response.parse()
        assert_matches_type(VdbconnectorCreateResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Deasy) -> None:
        with client.console.vdbconnector.with_streaming_response.create(
            secret_name="secret_name",
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vdbconnector = response.parse()
            assert_matches_type(VdbconnectorCreateResponse, vdbconnector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        vdbconnector = client.console.vdbconnector.delete(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(VdbconnectorDeleteResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.console.vdbconnector.with_raw_response.delete(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vdbconnector = response.parse()
        assert_matches_type(VdbconnectorDeleteResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.console.vdbconnector.with_streaming_response.delete(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vdbconnector = response.parse()
            assert_matches_type(VdbconnectorDeleteResponse, vdbconnector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_delete_stats(self, client: Deasy) -> None:
        vdbconnector = client.console.vdbconnector.get_delete_stats(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(VdbconnectorGetDeleteStatsResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_delete_stats(self, client: Deasy) -> None:
        response = client.console.vdbconnector.with_raw_response.get_delete_stats(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vdbconnector = response.parse()
        assert_matches_type(VdbconnectorGetDeleteStatsResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_delete_stats(self, client: Deasy) -> None:
        with client.console.vdbconnector.with_streaming_response.get_delete_stats(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vdbconnector = response.parse()
            assert_matches_type(VdbconnectorGetDeleteStatsResponse, vdbconnector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVdbconnector:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasy) -> None:
        vdbconnector = await async_client.console.vdbconnector.create(
            secret_name="secret_name",
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(VdbconnectorCreateResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.vdbconnector.with_raw_response.create(
            secret_name="secret_name",
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vdbconnector = await response.parse()
        assert_matches_type(VdbconnectorCreateResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.vdbconnector.with_streaming_response.create(
            secret_name="secret_name",
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vdbconnector = await response.parse()
            assert_matches_type(VdbconnectorCreateResponse, vdbconnector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        vdbconnector = await async_client.console.vdbconnector.delete(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(VdbconnectorDeleteResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.vdbconnector.with_raw_response.delete(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vdbconnector = await response.parse()
        assert_matches_type(VdbconnectorDeleteResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.vdbconnector.with_streaming_response.delete(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vdbconnector = await response.parse()
            assert_matches_type(VdbconnectorDeleteResponse, vdbconnector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_delete_stats(self, async_client: AsyncDeasy) -> None:
        vdbconnector = await async_client.console.vdbconnector.get_delete_stats(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(VdbconnectorGetDeleteStatsResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_delete_stats(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.vdbconnector.with_raw_response.get_delete_stats(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vdbconnector = await response.parse()
        assert_matches_type(VdbconnectorGetDeleteStatsResponse, vdbconnector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_delete_stats(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.vdbconnector.with_streaming_response.get_delete_stats(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vdbconnector = await response.parse()
            assert_matches_type(VdbconnectorGetDeleteStatsResponse, vdbconnector, path=["response"])

        assert cast(Any, response.is_closed) is True
