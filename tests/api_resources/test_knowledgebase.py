# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from propulsionai import PropulsionAI, AsyncPropulsionAI
from propulsionai.types import KnowledgebaseCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgebase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PropulsionAI) -> None:
        knowledgebase = client.knowledgebase.create(
            name="name",
            project_id=0,
            tags="tags",
        )
        assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PropulsionAI) -> None:
        knowledgebase = client.knowledgebase.create(
            name="name",
            project_id=0,
            tags="tags",
            description="description",
        )
        assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PropulsionAI) -> None:
        response = client.knowledgebase.with_raw_response.create(
            name="name",
            project_id=0,
            tags="tags",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledgebase = response.parse()
        assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PropulsionAI) -> None:
        with client.knowledgebase.with_streaming_response.create(
            name="name",
            project_id=0,
            tags="tags",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledgebase = response.parse()
            assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledgebase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPropulsionAI) -> None:
        knowledgebase = await async_client.knowledgebase.create(
            name="name",
            project_id=0,
            tags="tags",
        )
        assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPropulsionAI) -> None:
        knowledgebase = await async_client.knowledgebase.create(
            name="name",
            project_id=0,
            tags="tags",
            description="description",
        )
        assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPropulsionAI) -> None:
        response = await async_client.knowledgebase.with_raw_response.create(
            name="name",
            project_id=0,
            tags="tags",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledgebase = await response.parse()
        assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPropulsionAI) -> None:
        async with async_client.knowledgebase.with_streaming_response.create(
            name="name",
            project_id=0,
            tags="tags",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledgebase = await response.parse()
            assert_matches_type(KnowledgebaseCreateResponse, knowledgebase, path=["response"])

        assert cast(Any, response.is_closed) is True
