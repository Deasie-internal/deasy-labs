# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.console import UserUpdateProfileResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_profile(self, client: DeasyLabs) -> None:
        user = client.console.user.update_profile(
            company="company",
            first_name="first_name",
            last_name="last_name",
            phone_number="phone_number",
            x_user="x-user",
        )
        assert_matches_type(UserUpdateProfileResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_profile(self, client: DeasyLabs) -> None:
        response = client.console.user.with_raw_response.update_profile(
            company="company",
            first_name="first_name",
            last_name="last_name",
            phone_number="phone_number",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateProfileResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_profile(self, client: DeasyLabs) -> None:
        with client.console.user.with_streaming_response.update_profile(
            company="company",
            first_name="first_name",
            last_name="last_name",
            phone_number="phone_number",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateProfileResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_profile(self, async_client: AsyncDeasyLabs) -> None:
        user = await async_client.console.user.update_profile(
            company="company",
            first_name="first_name",
            last_name="last_name",
            phone_number="phone_number",
            x_user="x-user",
        )
        assert_matches_type(UserUpdateProfileResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_profile(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.user.with_raw_response.update_profile(
            company="company",
            first_name="first_name",
            last_name="last_name",
            phone_number="phone_number",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateProfileResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_profile(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.user.with_streaming_response.update_profile(
            company="company",
            first_name="first_name",
            last_name="last_name",
            phone_number="phone_number",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateProfileResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
