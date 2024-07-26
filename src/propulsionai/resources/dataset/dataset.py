# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .item import (
    ItemResource,
    AsyncItemResource,
    ItemResourceWithRawResponse,
    AsyncItemResourceWithRawResponse,
    ItemResourceWithStreamingResponse,
    AsyncItemResourceWithStreamingResponse,
)
from ...types import dataset_create_params
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
from ...types.dataset_create_response import DatasetCreateResponse

__all__ = ["DatasetResource", "AsyncDatasetResource"]


class DatasetResource(SyncAPIResource):
    @cached_property
    def item(self) -> ItemResource:
        return ItemResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetResourceWithRawResponse:
        return DatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetResourceWithStreamingResponse:
        return DatasetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        settings: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCreateResponse:
        """
        Creates a new dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "settings": settings,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCreateResponse,
        )


class AsyncDatasetResource(AsyncAPIResource):
    @cached_property
    def item(self) -> AsyncItemResource:
        return AsyncItemResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetResourceWithRawResponse:
        return AsyncDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetResourceWithStreamingResponse:
        return AsyncDatasetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        settings: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCreateResponse:
        """
        Creates a new dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "metadata": metadata,
                    "settings": settings,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCreateResponse,
        )


class DatasetResourceWithRawResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_raw_response_wrapper(
            dataset.create,
        )

    @cached_property
    def item(self) -> ItemResourceWithRawResponse:
        return ItemResourceWithRawResponse(self._dataset.item)


class AsyncDatasetResourceWithRawResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_raw_response_wrapper(
            dataset.create,
        )

    @cached_property
    def item(self) -> AsyncItemResourceWithRawResponse:
        return AsyncItemResourceWithRawResponse(self._dataset.item)


class DatasetResourceWithStreamingResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_streamed_response_wrapper(
            dataset.create,
        )

    @cached_property
    def item(self) -> ItemResourceWithStreamingResponse:
        return ItemResourceWithStreamingResponse(self._dataset.item)


class AsyncDatasetResourceWithStreamingResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_streamed_response_wrapper(
            dataset.create,
        )

    @cached_property
    def item(self) -> AsyncItemResourceWithStreamingResponse:
        return AsyncItemResourceWithStreamingResponse(self._dataset.item)
