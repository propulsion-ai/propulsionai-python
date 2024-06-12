# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Callable, Iterable, Optional

import httpx

from ..types import model_chat_params
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
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
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
        This endpoint runs a model with the specified tools and messages.

        Args:
          wait: Whether to wait for the response or not.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          temperature: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

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
                    "max_tokens": max_tokens,
                    "n": n,
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

    async def chat_auto(
        self,
        model_id: str,
        *,
        messages: Iterable[model_chat_params.Message],
        model: str,
        stream: bool,
        wait: bool | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
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
        available_function_map: Dict[str, Callable[..., Any]],
    ) -> ModelChatResponse:
        if not model_id:
            raise ValueError(f"Expected a non-empty value for `model_id` but received {model_id!r}")
        
        if not tools or not available_function_map:
            initial_response: ModelChatResponse = self._post(
                f"/api/v1/{model_id}/run",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "model": model,
                        "stream": stream,
                        "max_tokens": max_tokens,
                        "n": n,
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
            return initial_response
        
        initial_response = self._post(
            f"/api/v1/{model_id}/run",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "stream": stream,
                    "max_tokens": max_tokens,
                    "n": n,
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
        # check that choices and content are present
        initial_message: str = ""
        if (
            not initial_response.choices
            or not initial_response.choices[0].message
            or not initial_response.choices[0].message.content
        ):
            initial_message = "Function call by user"
        else:
            initial_message = initial_response.choices[0].message.content
            
        # if initial response has tool_calls, then loop through the tool_calls and call the tools
        # if there are no tool_calls, then return the initial response
        if initial_response.tool_calls:
            for tool_call in initial_response.tool_calls:
                function_name: str | None = str(tool_call.function["name"]) if tool_call.function else None
                function_params = tool_call.function["parameters"] if tool_call.function else None
                if(not function_name):
                    raise ValueError(f"Function name is sent by th model, it is required to call the function.")
                # Check if available_function_map[function_name] exists
                if function_name not in available_function_map:
                    raise ValueError(f"Function {function_name} is not available in the available_function_map.")
                
                function_response = await available_function_map[function_name](function_params)
                # append response to the messages
                messages = list(messages)
                messages.append({"role": "assistant", "content": initial_message})
                messages.append({"role": "user", "content": function_response})
                final_response: ModelChatResponse = self._post(
                    f"/api/v1/{model_id}/run",
                    body=maybe_transform(
                        {
                            "messages": messages,
                            "model": model,
                            "stream": stream,
                            "max_tokens": max_tokens,
                            "n": n,
                            "temperature": temperature,
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
                return final_response
        else:
            return initial_response
        return initial_response


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
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
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
        This endpoint runs a model with the specified tools and messages.

        Args:
          wait: Whether to wait for the response or not.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          temperature: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

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
                    "max_tokens": max_tokens,
                    "n": n,
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


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.chat = to_raw_response_wrapper(
            models.chat,
        )


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.chat = async_to_raw_response_wrapper(
            models.chat,
        )


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.chat = to_streamed_response_wrapper(
            models.chat,
        )


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.chat = async_to_streamed_response_wrapper(
            models.chat,
        )
