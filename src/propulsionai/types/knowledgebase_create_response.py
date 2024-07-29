# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["KnowledgebaseCreateResponse"]


class KnowledgebaseCreateResponse(BaseModel):
    id: Optional[int] = None

    message: Optional[str] = None
