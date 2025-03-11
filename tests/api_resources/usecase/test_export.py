# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types.usecase import ExportToVdbResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_metadata(self, client: DeasyLabs) -> None:
        export = client.usecase.export.metadata(
            vector_db_config={},
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_metadata_with_all_params(self, client: DeasyLabs) -> None:
        export = client.usecase.export.metadata(
            vector_db_config={},
            export_both_levels=True,
            export_chunk_level=True,
            export_file_level=True,
            export_format="json",
            selected_metadata_fields=["string"],
            usecase_id="usecase_id",
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_metadata(self, client: DeasyLabs) -> None:
        response = client.usecase.export.with_raw_response.metadata(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_metadata(self, client: DeasyLabs) -> None:
        with client.usecase.export.with_streaming_response.metadata(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(object, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_to_vdb(self, client: DeasyLabs) -> None:
        export = client.usecase.export.to_vdb(
            target_vector_db_config={},
        )
        assert_matches_type(ExportToVdbResponse, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_to_vdb_with_all_params(self, client: DeasyLabs) -> None:
        export = client.usecase.export.to_vdb(
            target_vector_db_config={},
            export_level="file",
            export_tags=[{}],
            ori_vector_db_config={},
            usecase_id="usecase_id",
        )
        assert_matches_type(ExportToVdbResponse, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_to_vdb(self, client: DeasyLabs) -> None:
        response = client.usecase.export.with_raw_response.to_vdb(
            target_vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportToVdbResponse, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_to_vdb(self, client: DeasyLabs) -> None:
        with client.usecase.export.with_streaming_response.to_vdb(
            target_vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportToVdbResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExport:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_metadata(self, async_client: AsyncDeasyLabs) -> None:
        export = await async_client.usecase.export.metadata(
            vector_db_config={},
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_metadata_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        export = await async_client.usecase.export.metadata(
            vector_db_config={},
            export_both_levels=True,
            export_chunk_level=True,
            export_file_level=True,
            export_format="json",
            selected_metadata_fields=["string"],
            usecase_id="usecase_id",
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.export.with_raw_response.metadata(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.export.with_streaming_response.metadata(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(object, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_to_vdb(self, async_client: AsyncDeasyLabs) -> None:
        export = await async_client.usecase.export.to_vdb(
            target_vector_db_config={},
        )
        assert_matches_type(ExportToVdbResponse, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_to_vdb_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        export = await async_client.usecase.export.to_vdb(
            target_vector_db_config={},
            export_level="file",
            export_tags=[{}],
            ori_vector_db_config={},
            usecase_id="usecase_id",
        )
        assert_matches_type(ExportToVdbResponse, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_to_vdb(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.usecase.export.with_raw_response.to_vdb(
            target_vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportToVdbResponse, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_to_vdb(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.usecase.export.with_streaming_response.to_vdb(
            target_vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportToVdbResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True
