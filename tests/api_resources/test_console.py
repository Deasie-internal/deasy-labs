# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import ConsoleFetchTiersResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsole:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_fetch_tiers(self, client: Deasy) -> None:
        console = client.console.fetch_tiers(
            x_user="x-user",
        )
        assert_matches_type(ConsoleFetchTiersResponse, console, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_fetch_tiers(self, client: Deasy) -> None:
        response = client.console.with_raw_response.fetch_tiers(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = response.parse()
        assert_matches_type(ConsoleFetchTiersResponse, console, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_fetch_tiers(self, client: Deasy) -> None:
        with client.console.with_streaming_response.fetch_tiers(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = response.parse()
            assert_matches_type(ConsoleFetchTiersResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConsole:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_fetch_tiers(self, async_client: AsyncDeasy) -> None:
        console = await async_client.console.fetch_tiers(
            x_user="x-user",
        )
        assert_matches_type(ConsoleFetchTiersResponse, console, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_fetch_tiers(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.with_raw_response.fetch_tiers(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = await response.parse()
        assert_matches_type(ConsoleFetchTiersResponse, console, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_fetch_tiers(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.with_streaming_response.fetch_tiers(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = await response.parse()
            assert_matches_type(ConsoleFetchTiersResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True
