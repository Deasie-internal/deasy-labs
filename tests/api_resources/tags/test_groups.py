# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from tests.utils import assert_matches_type
from Deasy.types.tags import (
    GroupListResponse,
    GroupCreateResponse,
    GroupDeleteResponse,
    GroupUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Deasy) -> None:
        group = client.tags.groups.create(
            group_name="group_name",
            x_user="x-user",
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Deasy) -> None:
        group = client.tags.groups.create(
            group_name="group_name",
            x_user="x-user",
            group_description="group_description",
            tag_ids=["string"],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Deasy) -> None:
        response = client.tags.groups.with_raw_response.create(
            group_name="group_name",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Deasy) -> None:
        with client.tags.groups.with_streaming_response.create(
            group_name="group_name",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Deasy) -> None:
        group = client.tags.groups.update(
            group_id="group_id",
            x_user="x-user",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Deasy) -> None:
        group = client.tags.groups.update(
            group_id="group_id",
            x_user="x-user",
            group_description="group_description",
            group_name="group_name",
            tag_ids=["string"],
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Deasy) -> None:
        response = client.tags.groups.with_raw_response.update(
            group_id="group_id",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Deasy) -> None:
        with client.tags.groups.with_streaming_response.update(
            group_id="group_id",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Deasy) -> None:
        group = client.tags.groups.list(
            x_user="x-user",
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Deasy) -> None:
        response = client.tags.groups.with_raw_response.list(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Deasy) -> None:
        with client.tags.groups.with_streaming_response.list(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupListResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        group = client.tags.groups.delete(
            group_id="group_id",
            x_user="x-user",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Deasy) -> None:
        group = client.tags.groups.delete(
            group_id="group_id",
            x_user="x-user",
            delete_associated_tags=True,
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.tags.groups.with_raw_response.delete(
            group_id="group_id",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.tags.groups.with_streaming_response.delete(
            group_id="group_id",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.create(
            group_name="group_name",
            x_user="x-user",
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.create(
            group_name="group_name",
            x_user="x-user",
            group_description="group_description",
            tag_ids=["string"],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasy) -> None:
        response = await async_client.tags.groups.with_raw_response.create(
            group_name="group_name",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasy) -> None:
        async with async_client.tags.groups.with_streaming_response.create(
            group_name="group_name",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.update(
            group_id="group_id",
            x_user="x-user",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.update(
            group_id="group_id",
            x_user="x-user",
            group_description="group_description",
            group_name="group_name",
            tag_ids=["string"],
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDeasy) -> None:
        response = await async_client.tags.groups.with_raw_response.update(
            group_id="group_id",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDeasy) -> None:
        async with async_client.tags.groups.with_streaming_response.update(
            group_id="group_id",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.list(
            x_user="x-user",
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasy) -> None:
        response = await async_client.tags.groups.with_raw_response.list(
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasy) -> None:
        async with async_client.tags.groups.with_streaming_response.list(
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupListResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.delete(
            group_id="group_id",
            x_user="x-user",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncDeasy) -> None:
        group = await async_client.tags.groups.delete(
            group_id="group_id",
            x_user="x-user",
            delete_associated_tags=True,
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.tags.groups.with_raw_response.delete(
            group_id="group_id",
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.tags.groups.with_streaming_response.delete(
            group_id="group_id",
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True
