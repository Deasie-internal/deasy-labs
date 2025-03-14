# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import (
    DataListPaginatedResponse,
    DataGetDocumentTextResponse,
    DataGetVdbTotalFilesResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_document_text(self, client: Deasy) -> None:
        data = client.data.get_document_text(
            file_names=["string"],
            vector_db_config={},
        )
        assert_matches_type(DataGetDocumentTextResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_document_text(self, client: Deasy) -> None:
        response = client.data.with_raw_response.get_document_text(
            file_names=["string"],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert_matches_type(DataGetDocumentTextResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_document_text(self, client: Deasy) -> None:
        with client.data.with_streaming_response.get_document_text(
            file_names=["string"],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert_matches_type(DataGetDocumentTextResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_vdb_total_files(self, client: Deasy) -> None:
        data = client.data.get_vdb_total_files(
            vector_db_config={},
        )
        assert_matches_type(DataGetVdbTotalFilesResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_vdb_total_files(self, client: Deasy) -> None:
        response = client.data.with_raw_response.get_vdb_total_files(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert_matches_type(DataGetVdbTotalFilesResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_vdb_total_files(self, client: Deasy) -> None:
        with client.data.with_streaming_response.get_vdb_total_files(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert_matches_type(DataGetVdbTotalFilesResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_paginated(self, client: Deasy) -> None:
        data = client.data.list_paginated(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(DataListPaginatedResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_paginated_with_all_params(self, client: Deasy) -> None:
        data = client.data.list_paginated(
            vector_db_config={},
            x_user="x-user",
            entities_already_scrolled=["string"],
            group_by="group_by",
            hard_limit=0,
            limit=0,
            offset=0,
            scroll_limit=0,
            search_query="search_query",
        )
        assert_matches_type(DataListPaginatedResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_paginated(self, client: Deasy) -> None:
        response = client.data.with_raw_response.list_paginated(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert_matches_type(DataListPaginatedResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_paginated(self, client: Deasy) -> None:
        with client.data.with_streaming_response.list_paginated(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert_matches_type(DataListPaginatedResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_document_text(self, async_client: AsyncDeasy) -> None:
        data = await async_client.data.get_document_text(
            file_names=["string"],
            vector_db_config={},
        )
        assert_matches_type(DataGetDocumentTextResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_document_text(self, async_client: AsyncDeasy) -> None:
        response = await async_client.data.with_raw_response.get_document_text(
            file_names=["string"],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert_matches_type(DataGetDocumentTextResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_document_text(self, async_client: AsyncDeasy) -> None:
        async with async_client.data.with_streaming_response.get_document_text(
            file_names=["string"],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert_matches_type(DataGetDocumentTextResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_vdb_total_files(self, async_client: AsyncDeasy) -> None:
        data = await async_client.data.get_vdb_total_files(
            vector_db_config={},
        )
        assert_matches_type(DataGetVdbTotalFilesResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_vdb_total_files(self, async_client: AsyncDeasy) -> None:
        response = await async_client.data.with_raw_response.get_vdb_total_files(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert_matches_type(DataGetVdbTotalFilesResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_vdb_total_files(self, async_client: AsyncDeasy) -> None:
        async with async_client.data.with_streaming_response.get_vdb_total_files(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert_matches_type(DataGetVdbTotalFilesResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_paginated(self, async_client: AsyncDeasy) -> None:
        data = await async_client.data.list_paginated(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(DataListPaginatedResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_paginated_with_all_params(self, async_client: AsyncDeasy) -> None:
        data = await async_client.data.list_paginated(
            vector_db_config={},
            x_user="x-user",
            entities_already_scrolled=["string"],
            group_by="group_by",
            hard_limit=0,
            limit=0,
            offset=0,
            scroll_limit=0,
            search_query="search_query",
        )
        assert_matches_type(DataListPaginatedResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_paginated(self, async_client: AsyncDeasy) -> None:
        response = await async_client.data.with_raw_response.list_paginated(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert_matches_type(DataListPaginatedResponse, data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_paginated(self, async_client: AsyncDeasy) -> None:
        async with async_client.data.with_streaming_response.list_paginated(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert_matches_type(DataListPaginatedResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True
