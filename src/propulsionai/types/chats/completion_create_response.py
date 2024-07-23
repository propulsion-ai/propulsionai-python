# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CompletionCreateResponse", "Choice", "ChoiceMessage", "ToolCall", "ToolCallFunction", "Usage"]


class ChoiceMessage(BaseModel):
    content: str

    role: Literal["system", "user", "assistant", "tool"]


class Choice(BaseModel):
    index: Optional[int] = None

    message: Optional[ChoiceMessage] = None


class ToolCallFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, object]] = None


class ToolCall(BaseModel):
    function: Optional[ToolCallFunction] = None

    type: Optional[Literal["function"]] = None


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

    tool_calls: Optional[List[ToolCall]] = None

    usage: Optional[Usage] = None
