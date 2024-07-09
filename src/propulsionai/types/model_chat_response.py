# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelChatResponse", "Choice", "ChoiceMessage", "ToolCall", "ToolCallFunction", "Usage"]


class ChoiceMessage(BaseModel):
    content: Optional[str] = None

    role: Optional[str] = None


class Choice(BaseModel):
    index: Optional[int] = None

    message: Optional[ChoiceMessage] = None


class ToolCallFunction(BaseModel):
    name: str
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: Optional[str] = None
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Optional[Dict[str, object]] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](/docs/guides/function-calling) for examples, and the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for
    documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...
    def __getitem__(self, item: str) -> object:
        return getattr(self, item)


class ToolCall(BaseModel):
    function: Optional[ToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ModelChatResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    tool_calls: Optional[List[ToolCall]] = FieldInfo(alias="toolCalls", default=None)

    usage: Optional[Usage] = None
