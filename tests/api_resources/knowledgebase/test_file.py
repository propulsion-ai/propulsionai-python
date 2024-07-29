# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from propulsionai import PropulsionAI, AsyncPropulsionAI
from propulsionai.types.knowledgebase import FileCreateResponse, FileDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PropulsionAI) -> None:
        file = client.knowledgebase.file.create(
            knowledgebase_id=0,
            file=b"raw file contents",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PropulsionAI) -> None:
        response = client.knowledgebase.file.with_raw_response.create(
            knowledgebase_id=0,
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PropulsionAI) -> None:
        with client.knowledgebase.file.with_streaming_response.create(
            knowledgebase_id=0,
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PropulsionAI) -> None:
        file = client.knowledgebase.file.delete(
            file_id="file_id",
            knowledgebase_id=0,
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: PropulsionAI) -> None:
        response = client.knowledgebase.file.with_raw_response.delete(
            file_id="file_id",
            knowledgebase_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: PropulsionAI) -> None:
        with client.knowledgebase.file.with_streaming_response.delete(
            file_id="file_id",
            knowledgebase_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PropulsionAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.knowledgebase.file.with_raw_response.delete(
                file_id="",
                knowledgebase_id=0,
            )


class TestAsyncFile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPropulsionAI) -> None:
        file = await async_client.knowledgebase.file.create(
            knowledgebase_id=0,
            file=b"raw file contents",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPropulsionAI) -> None:
        response = await async_client.knowledgebase.file.with_raw_response.create(
            knowledgebase_id=0,
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPropulsionAI) -> None:
        async with async_client.knowledgebase.file.with_streaming_response.create(
            knowledgebase_id=0,
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPropulsionAI) -> None:
        file = await async_client.knowledgebase.file.delete(
            file_id="file_id",
            knowledgebase_id=0,
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPropulsionAI) -> None:
        response = await async_client.knowledgebase.file.with_raw_response.delete(
            file_id="file_id",
            knowledgebase_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPropulsionAI) -> None:
        async with async_client.knowledgebase.file.with_streaming_response.delete(
            file_id="file_id",
            knowledgebase_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPropulsionAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.knowledgebase.file.with_raw_response.delete(
                file_id="",
                knowledgebase_id=0,
            )
