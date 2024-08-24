# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemCreateParams"]


class ItemCreateParams(TypedDict, total=False):
    content: Required[str]
    """The content that you want to upload to the knowledgebase."""

    source: Required[str]
    """
    You should use this field to specify the source of the content like url,
    filename, etc. This will be used for citation purposes.
    """

    metadata: object
    """You can use this field to specify any metadata associated with the content."""
