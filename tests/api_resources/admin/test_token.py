# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.admin import ListResponse, CreateResponse, DeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Deasy) -> None:
        token = client.admin.token.create(
            username="username",
            x_token="x-token",
            x_user="x-user",
        )
        assert_matches_type(CreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Deasy) -> None:
        response = client.admin.token.with_raw_response.create(
            username="username",
            x_token="x-token",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(CreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Deasy) -> None:
        with client.admin.token.with_streaming_response.create(
            username="username",
            x_token="x-token",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(CreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Deasy) -> None:
        token = client.admin.token.list(
            x_token="x-token",
            x_user="x-user",
        )
        assert_matches_type(ListResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Deasy) -> None:
        response = client.admin.token.with_raw_response.list(
            x_token="x-token",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(ListResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Deasy) -> None:
        with client.admin.token.with_streaming_response.list(
            x_token="x-token",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(ListResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        token = client.admin.token.delete(
            token_id="token_id",
            x_token="x-token",
            x_user="x-user",
        )
        assert_matches_type(DeleteResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.admin.token.with_raw_response.delete(
            token_id="token_id",
            x_token="x-token",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(DeleteResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.admin.token.with_streaming_response.delete(
            token_id="token_id",
            x_token="x-token",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(DeleteResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Deasy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.admin.token.with_raw_response.delete(
                token_id="",
                x_token="x-token",
                x_user="x-user",
            )


class TestAsyncToken:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasy) -> None:
        token = await async_client.admin.token.create(
            username="username",
            x_token="x-token",
            x_user="x-user",
        )
        assert_matches_type(CreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasy) -> None:
        response = await async_client.admin.token.with_raw_response.create(
            username="username",
            x_token="x-token",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(CreateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasy) -> None:
        async with async_client.admin.token.with_streaming_response.create(
            username="username",
            x_token="x-token",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(CreateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasy) -> None:
        token = await async_client.admin.token.list(
            x_token="x-token",
            x_user="x-user",
        )
        assert_matches_type(ListResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasy) -> None:
        response = await async_client.admin.token.with_raw_response.list(
            x_token="x-token",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(ListResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasy) -> None:
        async with async_client.admin.token.with_streaming_response.list(
            x_token="x-token",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(ListResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        token = await async_client.admin.token.delete(
            token_id="token_id",
            x_token="x-token",
            x_user="x-user",
        )
        assert_matches_type(DeleteResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.admin.token.with_raw_response.delete(
            token_id="token_id",
            x_token="x-token",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(DeleteResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.admin.token.with_streaming_response.delete(
            token_id="token_id",
            x_token="x-token",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(DeleteResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDeasy) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.admin.token.with_raw_response.delete(
                token_id="",
                x_token="x-token",
                x_user="x-user",
            )
