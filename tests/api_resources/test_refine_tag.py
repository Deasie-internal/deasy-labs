# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import RefineTagRefineResponse
from Deasy_Labs._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRefineTag:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_refine(self, client: DeasyLabs) -> None:
        refine_tag = client.refine_tag.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                }
            },
            vector_db_config={},
        )
        assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_refine_with_all_params(self, client: DeasyLabs) -> None:
        refine_tag = client.refine_tag.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                    "available_values": ["string"],
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "examples": ["string"],
                    "max_values": 0,
                    "neg_examples": ["string"],
                    "retry_feedback": {},
                    "tag_id": "tag_id",
                    "tuned": 0,
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "username": "username",
                }
            },
            vector_db_config={},
            file_names=["string"],
        )
        assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_refine(self, client: DeasyLabs) -> None:
        response = client.refine_tag.with_raw_response.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                }
            },
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refine_tag = response.parse()
        assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_refine(self, client: DeasyLabs) -> None:
        with client.refine_tag.with_streaming_response.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                }
            },
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refine_tag = response.parse()
            assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRefineTag:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_refine(self, async_client: AsyncDeasyLabs) -> None:
        refine_tag = await async_client.refine_tag.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                }
            },
            vector_db_config={},
        )
        assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_refine_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        refine_tag = await async_client.refine_tag.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                    "available_values": ["string"],
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "examples": ["string"],
                    "max_values": 0,
                    "neg_examples": ["string"],
                    "retry_feedback": {},
                    "tag_id": "tag_id",
                    "tuned": 0,
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "username": "username",
                }
            },
            vector_db_config={},
            file_names=["string"],
        )
        assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_refine(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.refine_tag.with_raw_response.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                }
            },
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refine_tag = await response.parse()
        assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_refine(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.refine_tag.with_streaming_response.refine(
            endpoint_manager_config={},
            tag_to_refine={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                }
            },
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refine_tag = await response.parse()
            assert_matches_type(RefineTagRefineResponse, refine_tag, path=["response"])

        assert cast(Any, response.is_closed) is True
