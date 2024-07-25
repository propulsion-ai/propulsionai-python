# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RecordCreateResponse"]


class RecordCreateResponse(BaseModel):
    message: Optional[str] = None

    task_id: Optional[str] = None
