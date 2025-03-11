# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import TagTextClassifyResponse
from Deasy_Labs._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTagText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify(self, client: DeasyLabs) -> None:
        tag_text = client.tag_text.classify(
            endpoint_manager_config={},
            text="text",
        )
        assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_with_all_params(self, client: DeasyLabs) -> None:
        tag_text = client.tag_text.classify(
            endpoint_manager_config={},
            text="text",
            max_retries=0,
            retry_temperature=0,
            tags={
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
        )
        assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify(self, client: DeasyLabs) -> None:
        response = client.tag_text.with_raw_response.classify(
            endpoint_manager_config={},
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_text = response.parse()
        assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify(self, client: DeasyLabs) -> None:
        with client.tag_text.with_streaming_response.classify(
            endpoint_manager_config={},
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_text = response.parse()
            assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTagText:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify(self, async_client: AsyncDeasyLabs) -> None:
        tag_text = await async_client.tag_text.classify(
            endpoint_manager_config={},
            text="text",
        )
        assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        tag_text = await async_client.tag_text.classify(
            endpoint_manager_config={},
            text="text",
            max_retries=0,
            retry_temperature=0,
            tags={
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
        )
        assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tag_text.with_raw_response.classify(
            endpoint_manager_config={},
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_text = await response.parse()
        assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tag_text.with_streaming_response.classify(
            endpoint_manager_config={},
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_text = await response.parse()
            assert_matches_type(TagTextClassifyResponse, tag_text, path=["response"])

        assert cast(Any, response.is_closed) is True
