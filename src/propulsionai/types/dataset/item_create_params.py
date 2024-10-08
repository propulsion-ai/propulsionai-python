# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ItemCreateParams",
    "Data",
    "DataMessage",
    "DataMessageContentUnionMember1",
    "DataMessageContentUnionMember1ImageURL",
    "DataTool",
    "DataToolFunction",
]


class ItemCreateParams(TypedDict, total=False):
    data: Required[Data]

    dataset_id: Required[int]


class DataMessageContentUnionMember1ImageURL(TypedDict, total=False):
    url: str


class DataMessageContentUnionMember1(TypedDict, total=False):
    image_url: DataMessageContentUnionMember1ImageURL

    text: str

    type: Literal["text", "image_url"]


class DataMessage(TypedDict, total=False):
    content: Union[str, Iterable[DataMessageContentUnionMember1]]

    role: Literal["system", "user", "assistant", "tool"]


class DataToolFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class DataTool(TypedDict, total=False):
    function: Required[DataToolFunction]

    type: Required[Literal["function"]]


class Data(TypedDict, total=False):
    chosen: Optional[str]

    history: Optional[Iterable[List[str]]]

    images: Optional[str]

    kto_tag: Optional[str]

    messages: Iterable[DataMessage]

    prompt: Optional[str]

    query: Optional[str]

    rejected: Optional[str]

    response: Optional[str]

    system: Optional[str]

    tools: Optional[Iterable[DataTool]]
