# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    chosen: str
    """The column name in the dataset containing the chosen answers."""

    history: str
    """The column name in the dataset containing the histories."""

    images: str
    """The column name in the dataset containing the image inputs."""

    kto_tag: str
    """The column name in the dataset containing the kto tags."""

    messages: str
    """The column name in the dataset containing the messages."""

    prompt: str
    """The column name in the dataset containing the prompts."""

    query: str
    """The column name in the dataset containing the queries."""

    rejected: str
    """The column name in the dataset containing the rejected answers."""

    response: str
    """The column name in the dataset containing the responses."""

    system: str
    """The column name in the dataset containing the system prompts."""

    tools: str
    """The column name in the dataset containing the tool descriptions."""
