# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["DatasetCreateResponse", "Dataset"]


class Dataset(BaseModel):
    id: Optional[float] = None

    created: Optional[int] = None

    description: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    project_id: Optional[float] = None

    settings: Optional[Dict[str, object]] = None

    updated: Optional[int] = None


class DatasetCreateResponse(BaseModel):
    id: Optional[float] = None

    dataset: Optional[Dataset] = None

    message: Optional[str] = None
