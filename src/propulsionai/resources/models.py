# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import model_ep_params, model_chat_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.model_ep_response import ModelEpResponse
from ..types.model_chat_response import ModelChatResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self)

    def chat(
        self,
        model_id: str,
        *,
        messages: Iterable[model_chat_params.Message],
        model: str,
        stream: bool,
        wait: bool | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: model_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[model_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelChatResponse:
        """
        Run a model with specified tools and messages.

        Args:
          wait: Whether to wait for the response or not.

          knowledgebases: A list of knowledgebase IDs to use in the model.

          max_tokens: The maximum number of tokens that can be generated in the chat completion.

          n: How many chat completion choices to generate for each input message.

          task_id: Optional task ID associated with the request.

          temperature: An alternative to sampling with temperature, called nucleus sampling.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_p: An alternative to sampling with temperature, called nucleus sampling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not model_id:
            raise ValueError(f"Expected a non-empty value for `model_id` but received {model_id!r}")
        return self._post(
            f"/api/v1/{model_id}/run",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                    "knowledgebases": knowledgebases,
                    "max_tokens": max_tokens,
                    "n": n,
                    "task_id": task_id,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                model_chat_params.ModelChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait": wait}, model_chat_params.ModelChatParams),
            ),
            cast_to=ModelChatResponse,
        )

    def ep(
        self,
        deployment_tag: str,
        *,
        messages: Iterable[model_ep_params.Message],
        model: str,
        stream: bool,
        wait: bool | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: model_ep_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[model_ep_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelEpResponse:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          wait: Whether to wait for the response or not.

          knowledgebases: A list of knowledgebase IDs to use in the model.

          max_tokens: The maximum number of tokens that can be generated in the chat completion.

          n: How many chat completion choices to generate for each input message.

          task_id: Optional task ID associated with the request.

          temperature: An alternative to sampling with temperature, called nucleus sampling.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_p: An alternative to sampling with temperature, called nucleus sampling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_tag:
            raise ValueError(f"Expected a non-empty value for `deployment_tag` but received {deployment_tag!r}")
        return self._post(
            f"/api/v1/chat/{deployment_tag}",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                    "knowledgebases": knowledgebases,
                    "max_tokens": max_tokens,
                    "n": n,
                    "task_id": task_id,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                model_ep_params.ModelEpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait": wait}, model_ep_params.ModelEpParams),
            ),
            cast_to=ModelEpResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self)

    async def chat(
        self,
        model_id: str,
        *,
        messages: Iterable[model_chat_params.Message],
        model: str,
        stream: bool,
        wait: bool | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: model_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[model_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelChatResponse:
        """
        Run a model with specified tools and messages.

        Args:
          wait: Whether to wait for the response or not.

          knowledgebases: A list of knowledgebase IDs to use in the model.

          max_tokens: The maximum number of tokens that can be generated in the chat completion.

          n: How many chat completion choices to generate for each input message.

          task_id: Optional task ID associated with the request.

          temperature: An alternative to sampling with temperature, called nucleus sampling.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_p: An alternative to sampling with temperature, called nucleus sampling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not model_id:
            raise ValueError(f"Expected a non-empty value for `model_id` but received {model_id!r}")
        return await self._post(
            f"/api/v1/{model_id}/run",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                    "knowledgebases": knowledgebases,
                    "max_tokens": max_tokens,
                    "n": n,
                    "task_id": task_id,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                model_chat_params.ModelChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"wait": wait}, model_chat_params.ModelChatParams),
            ),
            cast_to=ModelChatResponse,
        )

    async def ep(
        self,
        deployment_tag: str,
        *,
        messages: Iterable[model_ep_params.Message],
        model: str,
        stream: bool,
        wait: bool | NotGiven = NOT_GIVEN,
        knowledgebases: List[str] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: model_ep_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[model_ep_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelEpResponse:
        """
        Call a deployment endpoint with specified tools and messages.

        Args:
          wait: Whether to wait for the response or not.

          knowledgebases: A list of knowledgebase IDs to use in the model.

          max_tokens: The maximum number of tokens that can be generated in the chat completion.

          n: How many chat completion choices to generate for each input message.

          task_id: Optional task ID associated with the request.

          temperature: An alternative to sampling with temperature, called nucleus sampling.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_p: An alternative to sampling with temperature, called nucleus sampling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_tag:
            raise ValueError(f"Expected a non-empty value for `deployment_tag` but received {deployment_tag!r}")
        return await self._post(
            f"/api/v1/chat/{deployment_tag}",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                    "knowledgebases": knowledgebases,
                    "max_tokens": max_tokens,
                    "n": n,
                    "task_id": task_id,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                model_ep_params.ModelEpParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"wait": wait}, model_ep_params.ModelEpParams),
            ),
            cast_to=ModelEpResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.chat = to_raw_response_wrapper(
            models.chat,
        )
        self.ep = to_raw_response_wrapper(
            models.ep,
        )


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.chat = async_to_raw_response_wrapper(
            models.chat,
        )
        self.ep = async_to_raw_response_wrapper(
            models.ep,
        )


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.chat = to_streamed_response_wrapper(
            models.chat,
        )
        self.ep = to_streamed_response_wrapper(
            models.ep,
        )


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.chat = async_to_streamed_response_wrapper(
            models.chat,
        )
        self.ep = async_to_streamed_response_wrapper(
            models.ep,
        )
