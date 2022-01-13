from typing import Any, Dict, Optional, Sequence, Type
from quo.errors import Outlier
from citus.pydantic import BaseModel, ValidationError, create_model
from citus.pydantic.error_wrappers import ErrorList



class HTTPExceptions(Outlier):
    def __init__(
            self,
            status_code: int,
            detail: str = None
            ) -> None:
        if detail is None:
            detail = http.HTTPStatus(status_code).phrase
        self.status_code = status_code
        self.detail = detail

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"

class HTTPException(StarletteHTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)
        self.headers = headers


RequestErrorModel: Type[BaseModel] = create_model("Request")
WebSocketErrorModel: Type[BaseModel] = create_model("WebSocket")


class RequestValidationError(ValidationError):
    def __init__(self, errors: Sequence[ErrorList], *, body: Any = None) -> None:
        self.body = body
        super().__init__(errors, RequestErrorModel)


class WebSocketRequestValidationError(ValidationError):
    def __init__(self, errors: Sequence[ErrorList]) -> None:
        super().__init__(errors, WebSocketErrorModel)

class ImportFromStringError(Outlier):
    pass
