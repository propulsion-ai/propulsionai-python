# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KnowledgebaseCreateParams"]


class KnowledgebaseCreateParams(TypedDict, total=False):
    name: Required[str]

    project_id: Required[float]

    tags: Required[str]

    description: str
