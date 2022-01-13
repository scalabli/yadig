from citus.encoders import jsonable_encoder
from citus.errors import RequestValidationError
from citus.errors import HTTPExceptions as HTTPException
from citus.starlette.requests import Request
from citus.starlette.responses import JSONResponse
from citus.starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    headers = getattr(exc, "headers", None)
    if headers:
        return JSONResponse(
            {"detail": exc.detail}, status_code=exc.status_code, headers=headers
        )
    else:
        return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": jsonable_encoder(exc.errors())},
    )
