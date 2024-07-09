# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ModelEpParams",
    "Message",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "Tool",
    "ToolFunction",
]


class ModelEpParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    stream: Required[bool]

    wait: bool
    """Whether to wait for the response or not."""

    knowledgebases: List[str]
    """A list of knowledgebase IDs to use in the model."""

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion."""

    n: Optional[int]
    """How many chat completion choices to generate for each input message."""

    task_id: str
    """Optional task ID associated with the request."""

    temperature: Optional[float]
    """An alternative to sampling with temperature, called nucleus sampling."""

    tool_choice: ToolChoice
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tool and instead generates a message. `auto` means the model can
    pick between generating a message or calling one or more tools. `required` means
    the model must call one or more tools.
    """

    tools: Iterable[Tool]
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for. A max of 128 functions are
    supported.
    """

    top_p: Optional[float]
    """An alternative to sampling with temperature, called nucleus sampling."""


class Message(TypedDict, total=False):
    content: str

    role: Literal["system", "user", "assistant", "tool"]


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object."""


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]


ToolChoice = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoice]


class ToolFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object."""


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""
