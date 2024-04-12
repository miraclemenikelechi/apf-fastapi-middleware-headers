import starlette.status as status
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from middlewares import log_request
from routes import router

server = FastAPI()


# routes
server.include_router(router)


# middlewares
# server.add_middleware(log_request)


@server.middleware("http")
async def middleware(request, call_next):
    """
    Middleware function to log HTTP requests.

    Parameters:
        request: Incoming HTTP request.
        call_next: The function to call to continue processing the request.

    Returns:
        HTTP response to the request.
    """
    response = await log_request(request, call_next)
    return response


@server.get("/")
async def root():
    """
    Redirects incoming GET requests to the API documentation page.
    """

    # Redirecting to the API documentation page using a 302 status code
    return RedirectResponse(
        url="/docs",
        status_code=status.HTTP_302_FOUND,
    )
