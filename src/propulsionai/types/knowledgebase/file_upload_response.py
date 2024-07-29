# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FileUploadResponse"]


class FileUploadResponse(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None
