# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import (
    ClassifyClassifyAllResponse,
    ClassifyClassifyFilesResponse,
)
from Deasy_Labs._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_all(self, client: DeasyLabs) -> None:
        classify = client.classify.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_all_with_all_params(self, client: DeasyLabs) -> None:
        classify = client.classify.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
            conditions=[{}],
            generate_file_tags=True,
            hierarchy={},
            job_id="job_id",
            llm_dry_run=True,
            overwrite=True,
            soft_run=True,
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
            total_data_sets=0,
            usecase_id="usecase_id",
        )
        assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify_all(self, client: DeasyLabs) -> None:
        response = client.classify.with_raw_response.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify_all(self, client: DeasyLabs) -> None:
        with client.classify.with_streaming_response.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_files(self, client: DeasyLabs) -> None:
        classify = client.classify.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_files_with_all_params(self, client: DeasyLabs) -> None:
        classify = client.classify.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
            file_names=["string"],
            generate_file_tags=True,
            hierarchy={},
            job_id="job_id",
            overwrite=True,
            soft_run=True,
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
            usecase_id="usecase_id",
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify_files(self, client: DeasyLabs) -> None:
        response = client.classify.with_raw_response.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify_files(self, client: DeasyLabs) -> None:
        with client.classify.with_streaming_response.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassify:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_all(self, async_client: AsyncDeasyLabs) -> None:
        classify = await async_client.classify.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_all_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        classify = await async_client.classify.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
            conditions=[{}],
            generate_file_tags=True,
            hierarchy={},
            job_id="job_id",
            llm_dry_run=True,
            overwrite=True,
            soft_run=True,
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
            total_data_sets=0,
            usecase_id="usecase_id",
        )
        assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify_all(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.classify.with_raw_response.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify_all(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.classify.with_streaming_response.classify_all(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyClassifyAllResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_files(self, async_client: AsyncDeasyLabs) -> None:
        classify = await async_client.classify.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_files_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        classify = await async_client.classify.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
            file_names=["string"],
            generate_file_tags=True,
            hierarchy={},
            job_id="job_id",
            overwrite=True,
            soft_run=True,
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
            usecase_id="usecase_id",
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify_files(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.classify.with_raw_response.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify_files(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.classify.with_streaming_response.classify_files(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True
