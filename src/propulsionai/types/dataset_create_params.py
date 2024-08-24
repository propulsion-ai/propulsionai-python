# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]

    description: str

    metadata: Dict[str, object]

    settings: Dict[str, object]
