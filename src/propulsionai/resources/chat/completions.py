# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from types import coroutine
from typing import (  # type: ignore
    List,
    Union,
    Iterable,
    Optional,
    Awaitable,
    Generator,
    AsyncIterator,
    AsyncGenerator,
    cast,
    overload,
)
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ..._streaming import Stream, AsyncStream
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...lib.tool_runner import runner, stream_runner
from ...lib.tool_runner_async import async_runner, async_stream_runner
from ...types.chat.completion_create_chunk import CompletionCreateChunk
from ...types.chat.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        deployment: str,
        messages: List[completion_create_params.Message],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Literal[True],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[CompletionCreateChunk]:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: bool,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse | Stream[CompletionCreateChunk]:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "deployment"], ["messages", "deployment", "stream"])
    def create(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse | Stream[CompletionCreateChunk]:
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "deployment": deployment,
                    "messages": messages,
                    "knowledgebases": knowledgebases,
                    "max_tokens": max_tokens,
                    "n": n,
                    "stream": stream,
                    "task_id": task_id,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
            stream=stream or False,
            stream_cls=Stream[CompletionCreateChunk],
        )

    # Run Tools
    @overload
    def run_tools(
        self,
        *,
        deployment: str,
        messages: List[completion_create_params.Message],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tools: List[completion_create_params.ToolInput],
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        tool_debug: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run_tools(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Literal[True],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: List[completion_create_params.ToolInput],
        top_p: float | NotGiven = NOT_GIVEN,
        tool_debug: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Generator[CompletionCreateChunk, None, None]:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "deployment", "tools"], ["messages", "deployment", "stream", "tools"])
    def run_tools(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: List[completion_create_params.ToolInput],
        top_p: float | NotGiven = NOT_GIVEN,
        tool_debug: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse | Generator[CompletionCreateChunk, None, None]:
        if stream == True:
            return stream_runner(
                create=self.create,
                deployment=deployment,
                messages=messages,
                tools=tools,
                stream=True,
                tool_debug=tool_debug,
                knowledgebases=knowledgebases,
                max_tokens=max_tokens,
                n=n,
                task_id=task_id,
                temperature=temperature,
                tool_choice=tool_choice,
                top_p=top_p,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
        return runner(
            create=self.create,
            deployment=deployment,
            messages=messages,
            tools=tools,
            stream=False,
            tool_debug=tool_debug,
            knowledgebases=knowledgebases,
            max_tokens=max_tokens,
            n=n,
            task_id=task_id,
            temperature=temperature,
            tool_choice=tool_choice,
            top_p=top_p,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        deployment: str,
        messages: List[completion_create_params.Message],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Literal[True],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[CompletionCreateChunk]:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: bool,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse | AsyncStream[CompletionCreateChunk]:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          top_p: Probability threshold for token selection in text generation, controlling output
              randomness.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "deployment"], ["messages", "deployment", "stream"])
    async def create(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[completion_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse | AsyncStream[CompletionCreateChunk]:
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "deployment": deployment,
                    "messages": messages,
                    "knowledgebases": knowledgebases,
                    "max_tokens": max_tokens,
                    "n": n,
                    "stream": stream,
                    "task_id": task_id,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            stream=stream or False,
            stream_cls=AsyncStream[CompletionCreateChunk],
            cast_to=CompletionCreateResponse,
        )

    # Run Tools
    @overload
    async def run_tools(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Literal[False],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: List[completion_create_params.ToolInput],
        top_p: float | NotGiven = NOT_GIVEN,
        tool_debug: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse: ...

    @overload
    async def run_tools(
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: Literal[True],
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: List[completion_create_params.ToolInput],
        top_p: float | NotGiven = NOT_GIVEN,
        tool_debug: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AwaitableAsyncGenerator: ...

    @required_args(["messages", "deployment", "stream", "tools"], ["messages", "deployment", "stream", "tools"])
    async def run_tools(  # type: ignore # TODO: Remove when issue is fixed
        self,
        *,
        messages: List[completion_create_params.Message],
        deployment: str,
        stream: bool,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: completion_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: List[completion_create_params.ToolInput],
        top_p: float | NotGiven = NOT_GIVEN,
        tool_debug: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Union[CompletionCreateResponse, AwaitableAsyncGenerator]:
        if stream == True:
            return AwaitableAsyncGenerator(
                async_stream_runner(
                    create=self.create,
                    deployment=deployment,
                    messages=messages,
                    tools=tools,
                    stream=True,
                    tool_debug=tool_debug,
                    knowledgebases=knowledgebases,
                    max_tokens=max_tokens,
                    n=n,
                    task_id=task_id,
                    temperature=temperature,
                    tool_choice=tool_choice,
                    top_p=top_p,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                )
            )
        return await async_runner(
            create=self.create,
            deployment=deployment,
            messages=messages,
            tools=tools,
            stream=False,
            tool_debug=tool_debug,
            knowledgebases=knowledgebases,
            max_tokens=max_tokens,
            n=n,
            task_id=task_id,
            temperature=temperature,
            tool_choice=tool_choice,
            top_p=top_p,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class AwaitableAsyncGenerator:
    def __init__(self, generator: AsyncGenerator[CompletionCreateChunk, None]):
        self.generator = generator

    def __await__(self) -> Awaitable[List[CompletionCreateChunk]]:
        async def wrapper() -> List[CompletionCreateChunk]:
            result: List[CompletionCreateChunk] = []
            async for item in self.generator:
                result.append(item)
            return result
        
        return cast(Awaitable[List[CompletionCreateChunk]], coroutine(wrapper))

    async def __aiter__(self) -> AsyncIterator[CompletionCreateChunk]:
        async for item in self.generator:
            yield item


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
