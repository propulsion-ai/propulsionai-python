# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..._base_client import (
    make_request_options,
)
from ...types.datasets import task_create_params

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        dataset_id: int,
        *,
        chosen: str | NotGiven = NOT_GIVEN,
        history: str | NotGiven = NOT_GIVEN,
        images: str | NotGiven = NOT_GIVEN,
        kto_tag: str | NotGiven = NOT_GIVEN,
        messages: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        rejected: str | NotGiven = NOT_GIVEN,
        response: str | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This endpoint creates a new task for the dataset with specific columns.

        Args:
          chosen: The column name in the dataset containing the chosen answers.

          history: The column name in the dataset containing the histories.

          images: The column name in the dataset containing the image inputs.

          kto_tag: The column name in the dataset containing the kto tags.

          messages: The column name in the dataset containing the messages.

          prompt: The column name in the dataset containing the prompts.

          query: The column name in the dataset containing the queries.

          rejected: The column name in the dataset containing the rejected answers.

          response: The column name in the dataset containing the responses.

          system: The column name in the dataset containing the system prompts.

          tools: The column name in the dataset containing the tool descriptions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/v1/dataset/{dataset_id}/task",
            body=maybe_transform(
                {
                    "chosen": chosen,
                    "history": history,
                    "images": images,
                    "kto_tag": kto_tag,
                    "messages": messages,
                    "prompt": prompt,
                    "query": query,
                    "rejected": rejected,
                    "response": response,
                    "system": system,
                    "tools": tools,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        dataset_id: int,
        *,
        chosen: str | NotGiven = NOT_GIVEN,
        history: str | NotGiven = NOT_GIVEN,
        images: str | NotGiven = NOT_GIVEN,
        kto_tag: str | NotGiven = NOT_GIVEN,
        messages: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        rejected: str | NotGiven = NOT_GIVEN,
        response: str | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This endpoint creates a new task for the dataset with specific columns.

        Args:
          chosen: The column name in the dataset containing the chosen answers.

          history: The column name in the dataset containing the histories.

          images: The column name in the dataset containing the image inputs.

          kto_tag: The column name in the dataset containing the kto tags.

          messages: The column name in the dataset containing the messages.

          prompt: The column name in the dataset containing the prompts.

          query: The column name in the dataset containing the queries.

          rejected: The column name in the dataset containing the rejected answers.

          response: The column name in the dataset containing the responses.

          system: The column name in the dataset containing the system prompts.

          tools: The column name in the dataset containing the tool descriptions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/v1/dataset/{dataset_id}/task",
            body=await async_maybe_transform(
                {
                    "chosen": chosen,
                    "history": history,
                    "images": images,
                    "kto_tag": kto_tag,
                    "messages": messages,
                    "prompt": prompt,
                    "query": query,
                    "rejected": rejected,
                    "response": response,
                    "system": system,
                    "tools": tools,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
