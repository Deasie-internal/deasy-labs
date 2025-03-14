# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import ContextualizeCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContextualize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Deasy) -> None:
        contextualize = client.contextualize.create(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Deasy) -> None:
        contextualize = client.contextualize.create(
            endpoint_manager_config={},
            vector_db_config={},
            dataslice_id="dataslice_id",
            file_names=["string"],
            ignore_untagged_files=True,
            job_id="job_id",
            overwrite=True,
            verbose=True,
        )
        assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Deasy) -> None:
        response = client.contextualize.with_raw_response.create(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contextualize = response.parse()
        assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Deasy) -> None:
        with client.contextualize.with_streaming_response.create(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contextualize = response.parse()
            assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContextualize:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasy) -> None:
        contextualize = await async_client.contextualize.create(
            endpoint_manager_config={},
            vector_db_config={},
        )
        assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeasy) -> None:
        contextualize = await async_client.contextualize.create(
            endpoint_manager_config={},
            vector_db_config={},
            dataslice_id="dataslice_id",
            file_names=["string"],
            ignore_untagged_files=True,
            job_id="job_id",
            overwrite=True,
            verbose=True,
        )
        assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasy) -> None:
        response = await async_client.contextualize.with_raw_response.create(
            endpoint_manager_config={},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contextualize = await response.parse()
        assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasy) -> None:
        async with async_client.contextualize.with_streaming_response.create(
            endpoint_manager_config={},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contextualize = await response.parse()
            assert_matches_type(ContextualizeCreateResponse, contextualize, path=["response"])

        assert cast(Any, response.is_closed) is True
