# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import SuggestHierarchySuggestResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuggestHierarchy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_suggest(self, client: Deasy) -> None:
        suggest_hierarchy = client.suggest_hierarchy.suggest(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_suggest_with_all_params(self, client: Deasy) -> None:
        suggest_hierarchy = client.suggest_hierarchy.suggest(
            endpoint_manager_config={},
            vector_db_config={},
            condition={},
            context_level="context_level",
            current_tree={},
            dataslice_id="dataslice_id",
            file_names=["string"],
            max_height=0,
            node={},
            use_existing_tags=True,
            use_extracted_tags=True,
            user_context="user_context",
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_suggest(self, client: Deasy) -> None:
        response = client.suggest_hierarchy.with_raw_response.suggest(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_hierarchy = response.parse()
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_suggest(self, client: Deasy) -> None:
        with client.suggest_hierarchy.with_streaming_response.suggest(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_hierarchy = response.parse()
            assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSuggestHierarchy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_suggest(self, async_client: AsyncDeasy) -> None:
        suggest_hierarchy = await async_client.suggest_hierarchy.suggest(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_suggest_with_all_params(self, async_client: AsyncDeasy) -> None:
        suggest_hierarchy = await async_client.suggest_hierarchy.suggest(
            endpoint_manager_config={},
            vector_db_config={},
            condition={},
            context_level="context_level",
            current_tree={},
            dataslice_id="dataslice_id",
            file_names=["string"],
            max_height=0,
            node={},
            use_existing_tags=True,
            use_extracted_tags=True,
            user_context="user_context",
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_suggest(self, async_client: AsyncDeasy) -> None:
        response = await async_client.suggest_hierarchy.with_raw_response.suggest(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_hierarchy = await response.parse()
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_suggest(self, async_client: AsyncDeasy) -> None:
        async with async_client.suggest_hierarchy.with_streaming_response.suggest(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_hierarchy = await response.parse()
            assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

        assert cast(Any, response.is_closed) is True
