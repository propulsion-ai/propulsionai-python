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
from ...types.dataset import item_create_params
from ...types.dataset.item_create_response import ItemCreateResponse

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
        *,
        data: item_create_params.Data,
        dataset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """
        Creates a new item in a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset/item",
            body=maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
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
        *,
        data: item_create_params.Data,
        dataset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ItemCreateResponse:
        """
        Creates a new item in a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset/item",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
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
