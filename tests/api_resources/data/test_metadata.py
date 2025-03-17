# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.data import MetadataListResponse, MetadataDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Deasy) -> None:
        metadata = client.data.metadata.list(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataListResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Deasy) -> None:
        metadata = client.data.metadata.list(
            vector_db_config={},
            x_user="x-user",
            file_names=["string"],
            full_text_filters=["string"],
            group_by="group_by",
            limit=0,
            metadata_key_filters=["string"],
            metadata_keys=["string"],
            metadata_value_filters={"foo": ["string"]},
            point_ids=["string"],
        )
        assert_matches_type(MetadataListResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Deasy) -> None:
        response = client.data.metadata.with_raw_response.list(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataListResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Deasy) -> None:
        with client.data.metadata.with_streaming_response.list(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataListResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        metadata = client.data.metadata.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Deasy) -> None:
        metadata = client.data.metadata.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
            limit=0,
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.data.metadata.with_raw_response.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.data.metadata.with_streaming_response.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.data.metadata.list(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataListResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.data.metadata.list(
            vector_db_config={},
            x_user="x-user",
            file_names=["string"],
            full_text_filters=["string"],
            group_by="group_by",
            limit=0,
            metadata_key_filters=["string"],
            metadata_keys=["string"],
            metadata_value_filters={"foo": ["string"]},
            point_ids=["string"],
        )
        assert_matches_type(MetadataListResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasy) -> None:
        response = await async_client.data.metadata.with_raw_response.list(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataListResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasy) -> None:
        async with async_client.data.metadata.with_streaming_response.list(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataListResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.data.metadata.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.data.metadata.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
            limit=0,
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.data.metadata.with_raw_response.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.data.metadata.with_streaming_response.delete(
            file_names=["string"],
            metadata_keys=["string"],
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True
