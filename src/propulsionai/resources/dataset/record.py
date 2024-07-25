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
from ...types.dataset import record_create_params
from ...types.dataset.record_create_response import RecordCreateResponse

__all__ = ["RecordResource", "AsyncRecordResource"]


class RecordResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordResourceWithRawResponse:
        return RecordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordResourceWithStreamingResponse:
        return RecordResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: record_create_params.Data,
        dataset_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordCreateResponse:
        """
        Creates a new record in a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dataset/record",
            body=maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                record_create_params.RecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordCreateResponse,
        )


class AsyncRecordResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordResourceWithRawResponse:
        return AsyncRecordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordResourceWithStreamingResponse:
        return AsyncRecordResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: record_create_params.Data,
        dataset_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordCreateResponse:
        """
        Creates a new record in a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dataset/record",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                record_create_params.RecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordCreateResponse,
        )


class RecordResourceWithRawResponse:
    def __init__(self, record: RecordResource) -> None:
        self._record = record

        self.create = to_raw_response_wrapper(
            record.create,
        )


class AsyncRecordResourceWithRawResponse:
    def __init__(self, record: AsyncRecordResource) -> None:
        self._record = record

        self.create = async_to_raw_response_wrapper(
            record.create,
        )


class RecordResourceWithStreamingResponse:
    def __init__(self, record: RecordResource) -> None:
        self._record = record

        self.create = to_streamed_response_wrapper(
            record.create,
        )


class AsyncRecordResourceWithStreamingResponse:
    def __init__(self, record: AsyncRecordResource) -> None:
        self._record = record

        self.create = async_to_streamed_response_wrapper(
            record.create,
        )
