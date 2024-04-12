import starlette.status as status
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes import router

server = FastAPI()
server.include_router(router)


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