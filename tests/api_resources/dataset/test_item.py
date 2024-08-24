# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from propulsionai import PropulsionAI, AsyncPropulsionAI
from propulsionai.types.dataset import ItemCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PropulsionAI) -> None:
        item = client.dataset.item.create(
            data={},
            dataset_id=0,
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PropulsionAI) -> None:
        item = client.dataset.item.create(
            data={
                "query": "query",
                "tools": [
                    {
                        "type": "function",
                        "function": {
                            "description": "description",
                            "name": "name",
                            "parameters": {"foo": "bar"},
                        },
                    },
                    {
                        "type": "function",
                        "function": {
                            "description": "description",
                            "name": "name",
                            "parameters": {"foo": "bar"},
                        },
                    },
                    {
                        "type": "function",
                        "function": {
                            "description": "description",
                            "name": "name",
                            "parameters": {"foo": "bar"},
                        },
                    },
                ],
                "chosen": "chosen",
                "images": "images",
                "prompt": "prompt",
                "system": "system",
                "history": [
                    ["string", "string", "string"],
                    ["string", "string", "string"],
                    ["string", "string", "string"],
                ],
                "kto_tag": "kto_tag",
                "messages": [
                    {
                        "role": "system",
                        "content": "content",
                    },
                    {
                        "role": "system",
                        "content": "content",
                    },
                    {
                        "role": "system",
                        "content": "content",
                    },
                ],
                "rejected": "rejected",
                "response": "response",
            },
            dataset_id=0,
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PropulsionAI) -> None:
        response = client.dataset.item.with_raw_response.create(
            data={},
            dataset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PropulsionAI) -> None:
        with client.dataset.item.with_streaming_response.create(
            data={},
            dataset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncItem:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPropulsionAI) -> None:
        item = await async_client.dataset.item.create(
            data={},
            dataset_id=0,
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPropulsionAI) -> None:
        item = await async_client.dataset.item.create(
            data={
                "query": "query",
                "tools": [
                    {
                        "type": "function",
                        "function": {
                            "description": "description",
                            "name": "name",
                            "parameters": {"foo": "bar"},
                        },
                    },
                    {
                        "type": "function",
                        "function": {
                            "description": "description",
                            "name": "name",
                            "parameters": {"foo": "bar"},
                        },
                    },
                    {
                        "type": "function",
                        "function": {
                            "description": "description",
                            "name": "name",
                            "parameters": {"foo": "bar"},
                        },
                    },
                ],
                "chosen": "chosen",
                "images": "images",
                "prompt": "prompt",
                "system": "system",
                "history": [
                    ["string", "string", "string"],
                    ["string", "string", "string"],
                    ["string", "string", "string"],
                ],
                "kto_tag": "kto_tag",
                "messages": [
                    {
                        "role": "system",
                        "content": "content",
                    },
                    {
                        "role": "system",
                        "content": "content",
                    },
                    {
                        "role": "system",
                        "content": "content",
                    },
                ],
                "rejected": "rejected",
                "response": "response",
            },
            dataset_id=0,
        )
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPropulsionAI) -> None:
        response = await async_client.dataset.item.with_raw_response.create(
            data={},
            dataset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPropulsionAI) -> None:
        async with async_client.dataset.item.with_streaming_response.create(
            data={},
            dataset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True
