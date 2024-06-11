# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from propulsionai import PropulsionAI, AsyncPropulsionAI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PropulsionAI) -> None:
        task = client.datasets.tasks.create(
            0,
        )
        assert task is None

    @parametrize
    def test_method_create_with_all_params(self, client: PropulsionAI) -> None:
        task = client.datasets.tasks.create(
            0,
            chosen="string",
            history="string",
            images="string",
            kto_tag="string",
            messages="string",
            prompt="string",
            query="string",
            rejected="string",
            response="string",
            system="string",
            tools="string",
        )
        assert task is None

    @parametrize
    def test_raw_response_create(self, client: PropulsionAI) -> None:
        response = client.datasets.tasks.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert task is None

    @parametrize
    def test_streaming_response_create(self, client: PropulsionAI) -> None:
        with client.datasets.tasks.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPropulsionAI) -> None:
        task = await async_client.datasets.tasks.create(
            0,
        )
        assert task is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPropulsionAI) -> None:
        task = await async_client.datasets.tasks.create(
            0,
            chosen="string",
            history="string",
            images="string",
            kto_tag="string",
            messages="string",
            prompt="string",
            query="string",
            rejected="string",
            response="string",
            system="string",
            tools="string",
        )
        assert task is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPropulsionAI) -> None:
        response = await async_client.datasets.tasks.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert task is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPropulsionAI) -> None:
        async with async_client.datasets.tasks.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True
