# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.metadata import (
    StandardizeGetTagDistributionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStandardize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DeasyLabs) -> None:
        standardize = client.metadata.standardize.list(
            vector_db_config={},
        )
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DeasyLabs) -> None:
        response = client.metadata.standardize.with_raw_response.list(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standardize = response.parse()
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DeasyLabs) -> None:
        with client.metadata.standardize.with_streaming_response.list(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standardize = response.parse()
            assert_matches_type(object, standardize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_tag_distribution(self, client: DeasyLabs) -> None:
        standardize = client.metadata.standardize.get_tag_distribution(
            tag_id="tag_id",
            vector_db_config={},
        )
        assert_matches_type(StandardizeGetTagDistributionResponse, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_tag_distribution(self, client: DeasyLabs) -> None:
        response = client.metadata.standardize.with_raw_response.get_tag_distribution(
            tag_id="tag_id",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standardize = response.parse()
        assert_matches_type(StandardizeGetTagDistributionResponse, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_tag_distribution(self, client: DeasyLabs) -> None:
        with client.metadata.standardize.with_streaming_response.get_tag_distribution(
            tag_id="tag_id",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standardize = response.parse()
            assert_matches_type(StandardizeGetTagDistributionResponse, standardize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_insert(self, client: DeasyLabs) -> None:
        standardize = client.metadata.standardize.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
        )
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_insert_with_all_params(self, client: DeasyLabs) -> None:
        standardize = client.metadata.standardize.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
            taxonomy_name="taxonomy_name",
        )
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_insert(self, client: DeasyLabs) -> None:
        response = client.metadata.standardize.with_raw_response.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standardize = response.parse()
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_insert(self, client: DeasyLabs) -> None:
        with client.metadata.standardize.with_streaming_response.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standardize = response.parse()
            assert_matches_type(object, standardize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStandardize:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasyLabs) -> None:
        standardize = await async_client.metadata.standardize.list(
            vector_db_config={},
        )
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.metadata.standardize.with_raw_response.list(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standardize = await response.parse()
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.metadata.standardize.with_streaming_response.list(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standardize = await response.parse()
            assert_matches_type(object, standardize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_tag_distribution(self, async_client: AsyncDeasyLabs) -> None:
        standardize = await async_client.metadata.standardize.get_tag_distribution(
            tag_id="tag_id",
            vector_db_config={},
        )
        assert_matches_type(StandardizeGetTagDistributionResponse, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_tag_distribution(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.metadata.standardize.with_raw_response.get_tag_distribution(
            tag_id="tag_id",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standardize = await response.parse()
        assert_matches_type(StandardizeGetTagDistributionResponse, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_tag_distribution(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.metadata.standardize.with_streaming_response.get_tag_distribution(
            tag_id="tag_id",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standardize = await response.parse()
            assert_matches_type(StandardizeGetTagDistributionResponse, standardize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_insert(self, async_client: AsyncDeasyLabs) -> None:
        standardize = await async_client.metadata.standardize.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
        )
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_insert_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        standardize = await async_client.metadata.standardize.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
            taxonomy_name="taxonomy_name",
        )
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.metadata.standardize.with_raw_response.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standardize = await response.parse()
        assert_matches_type(object, standardize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.metadata.standardize.with_streaming_response.insert(
            standard_mapping={},
            tag_id="tag_id",
            tag_name="tag_name",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standardize = await response.parse()
            assert_matches_type(object, standardize, path=["response"])

        assert cast(Any, response.is_closed) is True
