# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.knowledgebase import item_create_params
from ...types.knowledgebase.knowledgebase_item_response import KnowledgebaseItemResponse

__all__ = ["ItemResource", "AsyncItemResource"]


class ItemResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemResourceWithRawResponse:
        return ItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemResourceWithStreamingResponse:
        return ItemResourceWithStreamingResponse(self)

    def create(
        self,
        knowledgebase_code: str,
        *,
        content: str,
        source: str,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgebaseItemResponse:
        """
        Upload content to a knowledgebase.

        Args:
          content: The content that you want to upload to the knowledgebase.

          source: You should use this field to specify the source of the content like url,
              filename, etc. This will be used for citation purposes.

          metadata: You can use this field to specify any metadata associated with the content.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledgebase_code:
            raise ValueError(f"Expected a non-empty value for `knowledgebase_code` but received {knowledgebase_code!r}")
        return self._post(
            f"/knowledgebase/{knowledgebase_code}/item",
            body=maybe_transform(
                {
                    "content": content,
                    "source": source,
                    "metadata": metadata,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgebaseItemResponse,
        )


class AsyncItemResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemResourceWithRawResponse:
        return AsyncItemResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemResourceWithStreamingResponse:
        return AsyncItemResourceWithStreamingResponse(self)

    async def create(
        self,
        knowledgebase_code: str,
        *,
        content: str,
        source: str,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgebaseItemResponse:
        """
        Upload content to a knowledgebase.

        Args:
          content: The content that you want to upload to the knowledgebase.

          source: You should use this field to specify the source of the content like url,
              filename, etc. This will be used for citation purposes.

          metadata: You can use this field to specify any metadata associated with the content.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledgebase_code:
            raise ValueError(f"Expected a non-empty value for `knowledgebase_code` but received {knowledgebase_code!r}")
        return await self._post(
            f"/knowledgebase/{knowledgebase_code}/item",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "source": source,
                    "metadata": metadata,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgebaseItemResponse,
        )


class ItemResourceWithRawResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.create = to_raw_response_wrapper(
            item.create,
        )


class AsyncItemResourceWithRawResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.create = async_to_raw_response_wrapper(
            item.create,
        )


class ItemResourceWithStreamingResponse:
    def __init__(self, item: ItemResource) -> None:
        self._item = item

        self.create = to_streamed_response_wrapper(
            item.create,
        )


class AsyncItemResourceWithStreamingResponse:
    def __init__(self, item: AsyncItemResource) -> None:
        self._item = item

        self.create = async_to_streamed_response_wrapper(
            item.create,
        )
