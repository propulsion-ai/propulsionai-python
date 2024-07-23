# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CompletionCreateParams",
    "Message",
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


class Message(TypedDict, total=False):
    content: str

    role: Literal["system", "user", "assistant", "tool"]


class ToolChoiceChatCompletionNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class ToolChoiceChatCompletionNamedToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatCompletionNamedToolChoiceFunction]

    type: Required[Literal["function"]]


ToolChoice = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoice]


class ToolFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
