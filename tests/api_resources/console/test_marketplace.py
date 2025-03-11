# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.console import MarketplaceSignupResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketplace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_signup(self, client: DeasyLabs) -> None:
        marketplace = client.console.marketplace.signup(
            x_user="x-user",
        )
        assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_signup_with_all_params(self, client: DeasyLabs) -> None:
        marketplace = client.console.marketplace.signup(
            x_user="x-user",
            company="company",
            first_name="first_name",
            last_name="last_name",
            marketplace_token="marketplace_token",
        )
        assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_signup(self, client: DeasyLabs) -> None:
        response = client.console.marketplace.with_raw_response.signup(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketplace = response.parse()
        assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_signup(self, client: DeasyLabs) -> None:
        with client.console.marketplace.with_streaming_response.signup(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketplace = response.parse()
            assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketplace:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_signup(self, async_client: AsyncDeasyLabs) -> None:
        marketplace = await async_client.console.marketplace.signup(
            x_user="x-user",
        )
        assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_signup_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        marketplace = await async_client.console.marketplace.signup(
            x_user="x-user",
            company="company",
            first_name="first_name",
            last_name="last_name",
            marketplace_token="marketplace_token",
        )
        assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.marketplace.with_raw_response.signup(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketplace = await response.parse()
        assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.marketplace.with_streaming_response.signup(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketplace = await response.parse()
            assert_matches_type(MarketplaceSignupResponse, marketplace, path=["response"])

        assert cast(Any, response.is_closed) is True
