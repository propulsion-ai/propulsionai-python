# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .file import (
    FileResource,
    AsyncFileResource,
    FileResourceWithRawResponse,
    AsyncFileResourceWithRawResponse,
    FileResourceWithStreamingResponse,
    AsyncFileResourceWithStreamingResponse,
)
from ...types import knowledgebase_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.knowledgebase_create_response import KnowledgebaseCreateResponse

__all__ = ["KnowledgebaseResource", "AsyncKnowledgebaseResource"]


class KnowledgebaseResource(SyncAPIResource):
    @cached_property
    def file(self) -> FileResource:
        return FileResource(self._client)

    @cached_property
    def with_raw_response(self) -> KnowledgebaseResourceWithRawResponse:
        return KnowledgebaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgebaseResourceWithStreamingResponse:
        return KnowledgebaseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: float,
        tags: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgebaseCreateResponse:
        """
        Creates a new knowledgebase.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/knowledgebase",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "tags": tags,
                    "description": description,
                },
                knowledgebase_create_params.KnowledgebaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgebaseCreateResponse,
        )


class AsyncKnowledgebaseResource(AsyncAPIResource):
    @cached_property
    def file(self) -> AsyncFileResource:
        return AsyncFileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKnowledgebaseResourceWithRawResponse:
        return AsyncKnowledgebaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgebaseResourceWithStreamingResponse:
        return AsyncKnowledgebaseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: float,
        tags: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgebaseCreateResponse:
        """
        Creates a new knowledgebase.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/knowledgebase",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "tags": tags,
                    "description": description,
                },
                knowledgebase_create_params.KnowledgebaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgebaseCreateResponse,
        )


class KnowledgebaseResourceWithRawResponse:
    def __init__(self, knowledgebase: KnowledgebaseResource) -> None:
        self._knowledgebase = knowledgebase

        self.create = to_raw_response_wrapper(
            knowledgebase.create,
        )

    @cached_property
    def file(self) -> FileResourceWithRawResponse:
        return FileResourceWithRawResponse(self._knowledgebase.file)


class AsyncKnowledgebaseResourceWithRawResponse:
    def __init__(self, knowledgebase: AsyncKnowledgebaseResource) -> None:
        self._knowledgebase = knowledgebase

        self.create = async_to_raw_response_wrapper(
            knowledgebase.create,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithRawResponse:
        return AsyncFileResourceWithRawResponse(self._knowledgebase.file)


class KnowledgebaseResourceWithStreamingResponse:
    def __init__(self, knowledgebase: KnowledgebaseResource) -> None:
        self._knowledgebase = knowledgebase

        self.create = to_streamed_response_wrapper(
            knowledgebase.create,
        )

    @cached_property
    def file(self) -> FileResourceWithStreamingResponse:
        return FileResourceWithStreamingResponse(self._knowledgebase.file)


class AsyncKnowledgebaseResourceWithStreamingResponse:
    def __init__(self, knowledgebase: AsyncKnowledgebaseResource) -> None:
        self._knowledgebase = knowledgebase

        self.create = async_to_streamed_response_wrapper(
            knowledgebase.create,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithStreamingResponse:
        return AsyncFileResourceWithStreamingResponse(self._knowledgebase.file)
