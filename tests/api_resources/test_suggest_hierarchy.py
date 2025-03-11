# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import SuggestHierarchySuggestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuggestHierarchy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_suggest(self, client: DeasyLabs) -> None:
        suggest_hierarchy = client.suggest_hierarchy.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_suggest_with_all_params(self, client: DeasyLabs) -> None:
        suggest_hierarchy = client.suggest_hierarchy.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
            context="context",
            context_level="context_level",
            current_tree={},
            file_names=["string"],
            max_height=0,
            node={},
            tag_type="tag_type",
            total_files=0,
            use_existing_tags=True,
            use_extracted_tags=True,
            usecase_id="usecase_id",
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_suggest(self, client: DeasyLabs) -> None:
        response = client.suggest_hierarchy.with_raw_response.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_hierarchy = response.parse()
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_suggest(self, client: DeasyLabs) -> None:
        with client.suggest_hierarchy.with_streaming_response.suggest(
            condition={},
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
    async def test_method_suggest(self, async_client: AsyncDeasyLabs) -> None:
        suggest_hierarchy = await async_client.suggest_hierarchy.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_suggest_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        suggest_hierarchy = await async_client.suggest_hierarchy.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
            context="context",
            context_level="context_level",
            current_tree={},
            file_names=["string"],
            max_height=0,
            node={},
            tag_type="tag_type",
            total_files=0,
            use_existing_tags=True,
            use_extracted_tags=True,
            usecase_id="usecase_id",
        )
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_suggest(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.suggest_hierarchy.with_raw_response.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_hierarchy = await response.parse()
        assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_suggest(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.suggest_hierarchy.with_streaming_response.suggest(
            condition={},
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_hierarchy = await response.parse()
            assert_matches_type(SuggestHierarchySuggestResponse, suggest_hierarchy, path=["response"])

        assert cast(Any, response.is_closed) is True
