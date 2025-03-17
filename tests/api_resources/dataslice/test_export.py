# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_metadata(self, client: Deasy) -> None:
        export = client.dataslice.export.metadata(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_metadata_with_all_params(self, client: Deasy) -> None:
        export = client.dataslice.export.metadata(
            vdb_profile_name="vdb_profile_name",
            dataslice_id="dataslice_id",
            export_file_level=True,
            export_format="json",
            selected_metadata_fields=["string"],
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_metadata(self, client: Deasy) -> None:
        response = client.dataslice.export.with_raw_response.metadata(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_metadata(self, client: Deasy) -> None:
        with client.dataslice.export.with_streaming_response.metadata(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(object, export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExport:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_metadata(self, async_client: AsyncDeasy) -> None:
        export = await async_client.dataslice.export.metadata(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_metadata_with_all_params(self, async_client: AsyncDeasy) -> None:
        export = await async_client.dataslice.export.metadata(
            vdb_profile_name="vdb_profile_name",
            dataslice_id="dataslice_id",
            export_file_level=True,
            export_format="json",
            selected_metadata_fields=["string"],
        )
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncDeasy) -> None:
        response = await async_client.dataslice.export.with_raw_response.metadata(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(object, export, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncDeasy) -> None:
        async with async_client.dataslice.export.with_streaming_response.metadata(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(object, export, path=["response"])

        assert cast(Any, response.is_closed) is True
