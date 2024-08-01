# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Knowledgebase"]


class Knowledgebase(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None
