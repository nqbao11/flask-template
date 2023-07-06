from typing import Any

from .base import BaseSchema


class ErrorSchema(BaseSchema):
    error_message: str | None
    error_data: Any | None
    error_code: int | None
