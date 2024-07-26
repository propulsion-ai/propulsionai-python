# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from propulsionai import PropulsionAI, AsyncPropulsionAI
from propulsionai.types.chat import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PropulsionAI) -> None:
        completion = client.chat.completions.create(
            deployment="deployment",
            messages=[{
                    "role": "system",
                    "content": "System Bot",
                }, {
                    "role": "user",
                    "content": "Hello, world!",
                }],
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PropulsionAI) -> None:
        completion = client.chat.completions.create(
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
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PropulsionAI) -> None:
        response = client.chat.completions.with_raw_response.create(
            deployment="deployment",
            messages=[{
                    "role": "system",
                    "content": "System Bot",
                }, {
                    "role": "user",
                    "content": "Hello, world!",
                }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PropulsionAI) -> None:
        with client.chat.completions.with_streaming_response.create(
            deployment="deployment",
            messages=[{
                    "role": "system",
                    "content": "System Bot",
                }, {
                    "role": "user",
                    "content": "Hello, world!",
                }],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPropulsionAI) -> None:
        completion = await async_client.chat.completions.create(
            deployment="deployment",
            messages=[{
                    "role": "system",
                    "content": "System Bot",
                }, {
                    "role": "user",
                    "content": "Hello, world!",
                }],
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPropulsionAI) -> None:
        completion = await async_client.chat.completions.create(
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
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPropulsionAI) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            deployment="deployment",
            messages=[{
                    "role": "system",
                    "content": "System Bot",
                }, {
                    "role": "user",
                    "content": "Hello, world!",
                }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPropulsionAI) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            deployment="deployment",
            messages=[{
                    "role": "system",
                    "content": "System Bot",
                }, {
                    "role": "user",
                    "content": "Hello, world!",
                }],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
