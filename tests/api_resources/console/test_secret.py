# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.console import SecretGetResponse, SecretStoreResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecret:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Deasy) -> None:
        secret = client.console.secret.get(
            secret_name="secret_name",
            x_user="x-user",
        )
        assert_matches_type(SecretGetResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Deasy) -> None:
        response = client.console.secret.with_raw_response.get(
            secret_name="secret_name",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretGetResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Deasy) -> None:
        with client.console.secret.with_streaming_response.get(
            secret_name="secret_name",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretGetResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_store(self, client: Deasy) -> None:
        secret = client.console.secret.store(
            secret_name="secret_name",
            secret_value="secret_value",
            x_user="x-user",
        )
        assert_matches_type(SecretStoreResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_store(self, client: Deasy) -> None:
        response = client.console.secret.with_raw_response.store(
            secret_name="secret_name",
            secret_value="secret_value",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretStoreResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_store(self, client: Deasy) -> None:
        with client.console.secret.with_streaming_response.store(
            secret_name="secret_name",
            secret_value="secret_value",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretStoreResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecret:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncDeasy) -> None:
        secret = await async_client.console.secret.get(
            secret_name="secret_name",
            x_user="x-user",
        )
        assert_matches_type(SecretGetResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.secret.with_raw_response.get(
            secret_name="secret_name",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretGetResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.secret.with_streaming_response.get(
            secret_name="secret_name",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretGetResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_store(self, async_client: AsyncDeasy) -> None:
        secret = await async_client.console.secret.store(
            secret_name="secret_name",
            secret_value="secret_value",
            x_user="x-user",
        )
        assert_matches_type(SecretStoreResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_store(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.secret.with_raw_response.store(
            secret_name="secret_name",
            secret_value="secret_value",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretStoreResponse, secret, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_store(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.secret.with_streaming_response.store(
            secret_name="secret_name",
            secret_value="secret_value",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretStoreResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True
