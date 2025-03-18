# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import (
    MetadataDeleteResponse,
    MetadataUpsertResponse,
    MetadataListMetadataResponse,
    MetadataListPaginatedMetadataResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        metadata = client.metadata.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
            conditions={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            file_names=["string"],
            tags=["string"],
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_metadata(self, client: Deasy) -> None:
        metadata = client.metadata.list_metadata(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_metadata_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.list_metadata(
            vdb_profile_name="vdb_profile_name",
            conditions={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            include_chunk_level=True,
            tag_names=["string"],
        )
        assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_metadata(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.list_metadata(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_metadata(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.list_metadata(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_paginated_metadata(self, client: Deasy) -> None:
        metadata = client.metadata.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_paginated_metadata_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
            conditions={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            include_chunk_level=True,
            limit=0,
            offset=0,
            tag_names=["string"],
        )
        assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_paginated_metadata(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_paginated_metadata(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_upsert(self, client: Deasy) -> None:
        metadata = client.metadata.upsert(
            metadata={"foo": {"foo": {}}},
        )
        assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upsert_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.upsert(
            metadata={
                "foo": {
                    "foo": {
                        "chunk_level": {
                            "foo": {
                                "evidence": "evidence",
                                "values": ["string"],
                            }
                        },
                        "file_level": {
                            "evidence": "evidence",
                            "values": ["string"],
                        },
                    }
                }
            },
            dataslice_id="dataslice_id",
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upsert(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.upsert(
            metadata={"foo": {"foo": {}}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upsert(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.upsert(
            metadata={"foo": {"foo": {}}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
            conditions={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            file_names=["string"],
            tags=["string"],
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.delete(
            vdb_profile_name="vdb_profile_name",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_metadata(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.list_metadata(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_metadata_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.list_metadata(
            vdb_profile_name="vdb_profile_name",
            conditions={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            include_chunk_level=True,
            tag_names=["string"],
        )
        assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_metadata(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.list_metadata(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_metadata(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.list_metadata(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataListMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_paginated_metadata(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_paginated_metadata_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
            conditions={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            include_chunk_level=True,
            limit=0,
            offset=0,
            tag_names=["string"],
        )
        assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_paginated_metadata(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_paginated_metadata(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.list_paginated_metadata(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataListPaginatedMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_upsert(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.upsert(
            metadata={"foo": {"foo": {}}},
        )
        assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.upsert(
            metadata={
                "foo": {
                    "foo": {
                        "chunk_level": {
                            "foo": {
                                "evidence": "evidence",
                                "values": ["string"],
                            }
                        },
                        "file_level": {
                            "evidence": "evidence",
                            "values": ["string"],
                        },
                    }
                }
            },
            dataslice_id="dataslice_id",
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.upsert(
            metadata={"foo": {"foo": {}}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.upsert(
            metadata={"foo": {"foo": {}}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataUpsertResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True
