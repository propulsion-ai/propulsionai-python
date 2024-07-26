# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CompletionCreateResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageToolCall",
    "ChoiceMessageToolCallFunction",
    "Usage",
]


class ChoiceMessageToolCallFunction(BaseModel):
    name: str

    arguments: Optional[Dict[str, object]] = None

    description: Optional[str] = None


class ChoiceMessageToolCall(BaseModel):
    function: Optional[ChoiceMessageToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class ChoiceMessage(BaseModel):
    content: Optional[str] = None

    role: Optional[Literal["system", "user", "assistant", "tool"]] = None

    tool_calls: Optional[List[ChoiceMessageToolCall]] = None


class Choice(BaseModel):
    index: Optional[int] = None

    message: Optional[ChoiceMessage] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class CompletionCreateResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    task_id: Optional[str] = None

    usage: Optional[Usage] = None
