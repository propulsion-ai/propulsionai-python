# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from propulsionai import Propulsionai, AsyncPropulsionai
from propulsionai.types import ChatCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Propulsionai) -> None:
        chat = client.chats.create(
            deployment="deployment",
            messages=[{}, {}, {}],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Propulsionai) -> None:
        chat = client.chats.create(
            deployment="deployment",
            messages=[
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
            knowledgebases=["string", "string", "string"],
            max_tokens=0,
            n=1,
            stream=True,
            task_id="task_id",
            temperature=0,
            tool_choice="none",
            tools=[
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
            top_p=0,
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Propulsionai) -> None:
        response = client.chats.with_raw_response.create(
            deployment="deployment",
            messages=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Propulsionai) -> None:
        with client.chats.with_streaming_response.create(
            deployment="deployment",
            messages=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPropulsionai) -> None:
        chat = await async_client.chats.create(
            deployment="deployment",
            messages=[{}, {}, {}],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPropulsionai) -> None:
        chat = await async_client.chats.create(
            deployment="deployment",
            messages=[
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
            knowledgebases=["string", "string", "string"],
            max_tokens=0,
            n=1,
            stream=True,
            task_id="task_id",
            temperature=0,
            tool_choice="none",
            tools=[
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
            top_p=0,
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPropulsionai) -> None:
        response = await async_client.chats.with_raw_response.create(
            deployment="deployment",
            messages=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPropulsionai) -> None:
        async with async_client.chats.with_streaming_response.create(
            deployment="deployment",
            messages=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
