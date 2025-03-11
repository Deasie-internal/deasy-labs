# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.console import SubscriptionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: DeasyLabs) -> None:
        subscription = client.console.subscription.retrieve(
            x_user="x-user",
        )
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: DeasyLabs) -> None:
        response = client.console.subscription.with_raw_response.retrieve(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: DeasyLabs) -> None:
        with client.console.subscription.with_streaming_response.retrieve(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscription:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDeasyLabs) -> None:
        subscription = await async_client.console.subscription.retrieve(
            x_user="x-user",
        )
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.subscription.with_raw_response.retrieve(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.subscription.with_streaming_response.retrieve(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
