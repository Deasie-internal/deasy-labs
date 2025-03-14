# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.console.subscription import (
    StripeCancelResponse,
    StripeValidateResponse,
    StripeCreateSessionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStripe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: Deasy) -> None:
        stripe = client.console.subscription.stripe.cancel(
            x_user="x-user",
        )
        assert_matches_type(StripeCancelResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: Deasy) -> None:
        response = client.console.subscription.stripe.with_raw_response.cancel(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = response.parse()
        assert_matches_type(StripeCancelResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: Deasy) -> None:
        with client.console.subscription.stripe.with_streaming_response.cancel(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = response.parse()
            assert_matches_type(StripeCancelResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_session(self, client: Deasy) -> None:
        stripe = client.console.subscription.stripe.create_session(
            tier_id="tier_id",
            x_user="x-user",
        )
        assert_matches_type(StripeCreateSessionResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_session(self, client: Deasy) -> None:
        response = client.console.subscription.stripe.with_raw_response.create_session(
            tier_id="tier_id",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = response.parse()
        assert_matches_type(StripeCreateSessionResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_session(self, client: Deasy) -> None:
        with client.console.subscription.stripe.with_streaming_response.create_session(
            tier_id="tier_id",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = response.parse()
            assert_matches_type(StripeCreateSessionResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: Deasy) -> None:
        stripe = client.console.subscription.stripe.validate(
            x_user="x-user",
        )
        assert_matches_type(StripeValidateResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: Deasy) -> None:
        response = client.console.subscription.stripe.with_raw_response.validate(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = response.parse()
        assert_matches_type(StripeValidateResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: Deasy) -> None:
        with client.console.subscription.stripe.with_streaming_response.validate(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = response.parse()
            assert_matches_type(StripeValidateResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStripe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncDeasy) -> None:
        stripe = await async_client.console.subscription.stripe.cancel(
            x_user="x-user",
        )
        assert_matches_type(StripeCancelResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.subscription.stripe.with_raw_response.cancel(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = await response.parse()
        assert_matches_type(StripeCancelResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.subscription.stripe.with_streaming_response.cancel(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = await response.parse()
            assert_matches_type(StripeCancelResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_session(self, async_client: AsyncDeasy) -> None:
        stripe = await async_client.console.subscription.stripe.create_session(
            tier_id="tier_id",
            x_user="x-user",
        )
        assert_matches_type(StripeCreateSessionResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.subscription.stripe.with_raw_response.create_session(
            tier_id="tier_id",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = await response.parse()
        assert_matches_type(StripeCreateSessionResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.subscription.stripe.with_streaming_response.create_session(
            tier_id="tier_id",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = await response.parse()
            assert_matches_type(StripeCreateSessionResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncDeasy) -> None:
        stripe = await async_client.console.subscription.stripe.validate(
            x_user="x-user",
        )
        assert_matches_type(StripeValidateResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncDeasy) -> None:
        response = await async_client.console.subscription.stripe.with_raw_response.validate(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stripe = await response.parse()
        assert_matches_type(StripeValidateResponse, stripe, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncDeasy) -> None:
        async with async_client.console.subscription.stripe.with_streaming_response.validate(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stripe = await response.parse()
            assert_matches_type(StripeValidateResponse, stripe, path=["response"])

        assert cast(Any, response.is_closed) is True
