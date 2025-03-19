# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from deasy_python import DeasyLabs, AsyncDeasyLabs
from deasy_python.types import ClassifyBulkClassifyResponse
from deasy_python._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassifyBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify(self, client: DeasyLabs) -> None:
        classify_bulk = client.classify_bulk.classify(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_with_all_params(self, client: DeasyLabs) -> None:
        classify_bulk = client.classify_bulk.classify(
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
            hierarchy_data={},
            hierarchy_name="hierarchy_name",
            job_id="job_id",
            llm_profile_name="llm_profile_name",
            overwrite=True,
            tag_datas={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                    "available_values": ["string"],
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "date_format": "date_format",
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
            tag_names=["string"],
            total_data_sets=0,
        )
        assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify(self, client: DeasyLabs) -> None:
        response = client.classify_bulk.with_raw_response.classify(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify_bulk = response.parse()
        assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify(self, client: DeasyLabs) -> None:
        with client.classify_bulk.with_streaming_response.classify(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify_bulk = response.parse()
            assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassifyBulk:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify(self, async_client: AsyncDeasyLabs) -> None:
        classify_bulk = await async_client.classify_bulk.classify(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        classify_bulk = await async_client.classify_bulk.classify(
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
            hierarchy_data={},
            hierarchy_name="hierarchy_name",
            job_id="job_id",
            llm_profile_name="llm_profile_name",
            overwrite=True,
            tag_datas={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                    "available_values": ["string"],
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "date_format": "date_format",
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
            tag_names=["string"],
            total_data_sets=0,
        )
        assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.classify_bulk.with_raw_response.classify(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify_bulk = await response.parse()
        assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.classify_bulk.with_streaming_response.classify(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify_bulk = await response.parse()
            assert_matches_type(ClassifyBulkClassifyResponse, classify_bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
