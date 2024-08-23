from typing import List, Union, Optional, Any, Dict, Generator
from typing_extensions import Literal
import json
from ..types.chat.completion_create_response import CompletionCreateResponse

# from ..types.chat.completion_create_chunk import CompletionCreateChunk
# from .._streaming import Stream
from ..lib.tool_helper import generate_tool_from_function
from ..types.chat.completion_create_params import Message, ToolInput, Tool
from ..types.chat.completion_create_response import CompletionCreateResponse
from ..types.chat.completion_create_chunk import CompletionCreateChunk

# import httpx
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven  # type: ignore


# from typing import Any, Iterable, List, Union, Optional, Literal
# from typing_extensions import NotGiven
# import json

#
# from completion_create_chunk import CompletionCreateChunk


def runner(
    create: Any,
    messages: List[Message],
    deployment: str,
    tools: List[ToolInput],
    stream: Union[Optional[Literal[False]], Literal[True], NotGiven],
    tool_debug: bool = False,
    **kwargs: Any,
) -> CompletionCreateResponse:
    """
    Runs a conversation with tool usage.
    Args:
    deployment: The name of the model deployment to use for this request
    messages: The list of messages comprising the conversation so far.
    stream: If set, partial message deltas will be sent as a stream.
    knowledgebases: A list of knowledgebases to search over.
    max_tokens: The maximum number of tokens to generate.
    n: How many chat completion choices to generate for each input message.
    task_id: An optional task ID to associate with this completion.
    temperature: What sampling temperature to use.
    tool_choice: Controls which (if any) function is called by the model.
    tools: A list of tools the model may call.
    top_p: An alternative to sampling with temperature.
    tool_debug: Whether to enable tool debugging.
    extra_headers: Send extra headers
    extra_query: Add additional query parameters to the request
    extra_body: Add additional JSON properties to the request
    timeout: Override the client-level default timeout for this request, in seconds
    """

    try:
        processed_tools: List[Tool] = [generate_tool_from_function(tool) if callable(tool) else tool for tool in tools]
    except Exception as e:
        raise ValueError(f"Error processing tools: {str(e)}")

    if tool_debug:
        try:
            print("Processed Tool Definition:")
            print(json.dumps(processed_tools, indent=2))
        except json.JSONDecodeError:
            print("Warning: Unable to JSON encode processed tools for debugging.")

    try:
        response = create(
            deployment=deployment,
            messages=messages,
            tools=processed_tools,
            **kwargs,
        )
    except Exception as e:
        raise RuntimeError(f"Error calling create function: {str(e)}")

    try:
        response_json = json.loads(response.to_json())
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response from create function.")

    tool_responses: List[Dict[str, Any]] = []
    next_messages: List[Message] = list(messages)

    if "choices" in response_json:
        for choice in response_json["choices"]:
            if "message" not in choice:
                continue
            message = choice["message"]
            next_messages.append(message)
            if "tool_calls" not in message:
                return response
            if len(message["tool_calls"]) == 0:
                return response
            for tool_call in message["tool_calls"]:
                if "function" not in tool_call:
                    continue
                function = tool_call["function"]
                name = function.get("name")
                if not name:
                    continue
                for tool in tools:
                    if getattr(tool, "__name__", None) == name:
                        args = function.get("arguments", "{}")
                        try:
                            if isinstance(args, str):
                                args = json.loads(args)
                            tool_response: Any = tool(**args)
                            next_messages.append({"role": "tool", "tool_call_id": name, "content": str(tool_response)})
                        except Exception as e:
                            error_message = f"Error calling function '{name}': {str(e)}"
                            print(error_message)
                            tool_responses.append({"tool": name, "response": f"Error: {str(e)}"})
                        break
        return runner(create, next_messages, deployment, tools, stream, tool_debug, **kwargs)
    else:
        return response


def stream_runner(
    create: Any,
    messages: List[Message],
    deployment: str,
    tools: List[ToolInput],
    stream: bool = True,
    tool_debug: bool = False,
    **kwargs: Any,
) -> Generator[CompletionCreateChunk, None, None]:
    """
    Runs a conversation with tool usage and streams the results.
    Continues calling itself until there are no more tool calls.

    Args:
    create: The function to create chat completions.
    messages: The list of messages comprising the conversation so far.
    deployment: The name of the model deployment to use for this request.
    tools: A list of tools the model may call.
    **kwargs: Additional keyword arguments for the create function.

    Yields:
    Dict[str, Any]: Streamed chunks of the chat completion.
    """
    processed_tools = [
        (
            tool
            if not callable(tool)
            else {"type": "function", "function": {"name": tool.__name__, "description": tool.__doc__}}
        )
        for tool in tools
    ]
    response = create(deployment=deployment, messages=messages, tools=processed_tools, stream=True, **kwargs)
    full_response = ""
    current_tool_calls: List[Any] = []
    tool_call_content = ""
    for chunk in response:
        yield chunk
        for choice in chunk.choices:
            if choice.delta.content:
                full_response += choice.delta.content
            if choice.delta.tool_calls:
                for tool_call in choice.delta.tool_calls:
                    if len(current_tool_calls) <= tool_call.index:
                        current_tool_calls.append({"function": {"name": "", "arguments": ""}})
                    current_call = current_tool_calls[tool_call.index]
                    if tool_call.function:
                        call_content_desc = "Call "
                        if tool_call.function.name:
                            current_call["function"]["name"] = tool_call.function.name
                            call_content_desc += f"{tool_call.function.name} "
                        if tool_call.function.arguments:
                            current_call["function"]["arguments"] += tool_call.function.arguments
                            call_content_desc += f"with arguments: {tool_call.function.arguments}"
                        if choice.delta.content is not None:
                          tool_call_content += choice.delta.content
                        else:
                          tool_call_content += call_content_desc
                        
                        name = current_call["function"]["name"]
                        args = current_call["function"]["arguments"]
                        for tool in tools:
                          if getattr(tool, "__name__", None) == name:
                              try:
                                  args = json.loads(args) if isinstance(args, str) else args
                                  tool_response: Any = tool(**args if isinstance(args, dict) else {})
                                  messages.append(
                                      {"role": "tool", "tool_call_id": name, "content": str(tool_response)}
                                  )
                                  if tool_debug:
                                      print(f"Tool '{name}' called with args: {args}")
                                      print(f"Tool response: {tool_response}")
                              except Exception as e:
                                  error_message = f"Error calling function '{name}': {str(e)} with arguments: {args}"
                                  print(error_message)
                                  messages.append(
                                      {"role": "tool", "tool_call_id": name, "content": error_message}
                                  )
                              break
            if choice.finish_reason == "tool_calls":
                # Reset for next potential tool calls
                current_tool_calls = []
                yield from stream_runner(create, messages, deployment, tools, stream, tool_debug, **kwargs)