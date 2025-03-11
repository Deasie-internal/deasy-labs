# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_handle_stripe(self, client: DeasyLabs) -> None:
        webhook = client.console.webhook.handle_stripe()
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_handle_stripe(self, client: DeasyLabs) -> None:
        response = client.console.webhook.with_raw_response.handle_stripe()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_handle_stripe(self, client: DeasyLabs) -> None:
        with client.console.webhook.with_streaming_response.handle_stripe() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhook:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_handle_stripe(self, async_client: AsyncDeasyLabs) -> None:
        webhook = await async_client.console.webhook.handle_stripe()
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_handle_stripe(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.webhook.with_raw_response.handle_stripe()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_handle_stripe(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.webhook.with_streaming_response.handle_stripe() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
