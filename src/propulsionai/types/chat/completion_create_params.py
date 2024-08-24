# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Any, Callable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1ImageURL",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceFunction",
    "Tool",
    "ToolFunction",
]

class CompletionCreateParams(TypedDict, total=False):
    deployment: Required[str]

    messages: Required[Iterable[Message]]

    knowledgebases: List[str]

    max_tokens: int

    n: int

    stream: bool

    task_id: str

    temperature: float

    tool_choice: ToolChoice

    tools: Iterable[Tool]

    top_p: float
    """
    Probability threshold for token selection in text generation, controlling output
    randomness.
    """


class MessageContentUnionMember1ImageURL(TypedDict, total=False):
    url: str


class MessageContentUnionMember1(TypedDict, total=False):
    image_url: MessageContentUnionMember1ImageURL

    text: str

    type: Literal["text", "image_url"]


class Message(TypedDict, total=False):
    content: Union[str, Iterable[MessageContentUnionMember1]]

    role: Literal["system", "user", "assistant", "tool"]

    tool_call_id: str


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoice]


class ToolFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]


# ToolInput = Union[Callable[..., Any], Tool]
ToolInput = Callable[..., Any]