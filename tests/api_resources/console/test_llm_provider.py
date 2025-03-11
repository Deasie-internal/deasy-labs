# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.console import LlmProviderValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlmProvider:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: DeasyLabs) -> None:
        llm_provider = client.console.llm_provider.validate(
            endpoint_manager_config={},
            x_user="x-user",
        )
        assert_matches_type(LlmProviderValidateResponse, llm_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: DeasyLabs) -> None:
        response = client.console.llm_provider.with_raw_response.validate(
            endpoint_manager_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_provider = response.parse()
        assert_matches_type(LlmProviderValidateResponse, llm_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: DeasyLabs) -> None:
        with client.console.llm_provider.with_streaming_response.validate(
            endpoint_manager_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_provider = response.parse()
            assert_matches_type(LlmProviderValidateResponse, llm_provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLlmProvider:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncDeasyLabs) -> None:
        llm_provider = await async_client.console.llm_provider.validate(
            endpoint_manager_config={},
            x_user="x-user",
        )
        assert_matches_type(LlmProviderValidateResponse, llm_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.llm_provider.with_raw_response.validate(
            endpoint_manager_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_provider = await response.parse()
        assert_matches_type(LlmProviderValidateResponse, llm_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.llm_provider.with_streaming_response.validate(
            endpoint_manager_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_provider = await response.parse()
            assert_matches_type(LlmProviderValidateResponse, llm_provider, path=["response"])

        assert cast(Any, response.is_closed) is True
