# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from deasy_client import Deasy, AsyncDeasy
from deasy_client.types import SuggestSchemaCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuggestSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Deasy) -> None:
        suggest_schema = client.suggest_schema.create(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Deasy) -> None:
        suggest_schema = client.suggest_schema.create(
            vdb_profile_name="vdb_profile_name",
            condition={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                    "operator": "operator",
                },
            },
            context_level="context_level",
            current_tree={"foo": "bar"},
            dataslice_id="dataslice_id",
            file_names=["string"],
            graph_tag_type="open_ended",
            llm_profile_name="llm_profile_name",
            max_height=0,
            max_tags_per_level=0,
            min_tags_per_level=0,
            node={"foo": "bar"},
            set_max_values=True,
            use_existing_tags=True,
            use_extracted_tags=True,
            user_context="user_context",
        )
        assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Deasy) -> None:
        response = client.suggest_schema.with_raw_response.create(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_schema = response.parse()
        assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Deasy) -> None:
        with client.suggest_schema.with_streaming_response.create(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_schema = response.parse()
            assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSuggestSchema:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasy) -> None:
        suggest_schema = await async_client.suggest_schema.create(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeasy) -> None:
        suggest_schema = await async_client.suggest_schema.create(
            vdb_profile_name="vdb_profile_name",
            condition={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                    "operator": "operator",
                },
            },
            context_level="context_level",
            current_tree={"foo": "bar"},
            dataslice_id="dataslice_id",
            file_names=["string"],
            graph_tag_type="open_ended",
            llm_profile_name="llm_profile_name",
            max_height=0,
            max_tags_per_level=0,
            min_tags_per_level=0,
            node={"foo": "bar"},
            set_max_values=True,
            use_existing_tags=True,
            use_extracted_tags=True,
            user_context="user_context",
        )
        assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasy) -> None:
        response = await async_client.suggest_schema.with_raw_response.create(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_schema = await response.parse()
        assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasy) -> None:
        async with async_client.suggest_schema.with_streaming_response.create(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_schema = await response.parse()
            assert_matches_type(SuggestSchemaCreateResponse, suggest_schema, path=["response"])

        assert cast(Any, response.is_closed) is True
