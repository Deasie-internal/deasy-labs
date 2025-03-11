# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.console import (
    VectorDBValidateResponse,
    VectorDBCheckIndexesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorDB:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_indexes(self, client: DeasyLabs) -> None:
        vector_db = client.console.vector_db.check_indexes(
            body={},
            x_user="x-user",
        )
        assert_matches_type(VectorDBCheckIndexesResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_indexes(self, client: DeasyLabs) -> None:
        response = client.console.vector_db.with_raw_response.check_indexes(
            body={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = response.parse()
        assert_matches_type(VectorDBCheckIndexesResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_indexes(self, client: DeasyLabs) -> None:
        with client.console.vector_db.with_streaming_response.check_indexes(
            body={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = response.parse()
            assert_matches_type(VectorDBCheckIndexesResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: DeasyLabs) -> None:
        vector_db = client.console.vector_db.validate(
            body={},
            x_user="x-user",
        )
        assert_matches_type(VectorDBValidateResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: DeasyLabs) -> None:
        response = client.console.vector_db.with_raw_response.validate(
            body={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = response.parse()
        assert_matches_type(VectorDBValidateResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: DeasyLabs) -> None:
        with client.console.vector_db.with_streaming_response.validate(
            body={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = response.parse()
            assert_matches_type(VectorDBValidateResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVectorDB:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_indexes(self, async_client: AsyncDeasyLabs) -> None:
        vector_db = await async_client.console.vector_db.check_indexes(
            body={},
            x_user="x-user",
        )
        assert_matches_type(VectorDBCheckIndexesResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_indexes(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.vector_db.with_raw_response.check_indexes(
            body={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = await response.parse()
        assert_matches_type(VectorDBCheckIndexesResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_indexes(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.vector_db.with_streaming_response.check_indexes(
            body={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = await response.parse()
            assert_matches_type(VectorDBCheckIndexesResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncDeasyLabs) -> None:
        vector_db = await async_client.console.vector_db.validate(
            body={},
            x_user="x-user",
        )
        assert_matches_type(VectorDBValidateResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.console.vector_db.with_raw_response.validate(
            body={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_db = await response.parse()
        assert_matches_type(VectorDBValidateResponse, vector_db, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.console.vector_db.with_streaming_response.validate(
            body={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_db = await response.parse()
            assert_matches_type(VectorDBValidateResponse, vector_db, path=["response"])

        assert cast(Any, response.is_closed) is True
