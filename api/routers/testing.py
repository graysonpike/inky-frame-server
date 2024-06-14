import io
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from api.services import rendering as rendering_service


router = APIRouter()

openapi_metadata = {
    "name": "Testing",
    "description": "Endpoints for testing the operation of the server and frame.",
}


@router.get("/hello-world")
async def hello_world():
    """
    Returns a Hello World image for the Inky Frame to display.

    The image response is given in bytes using Transfer-Encoding, which allows the Pi Zero to
    receive the image in chunks via HTTP.
    """
    return StreamingResponse(rendering_service.get_hello_world_jpg(), media_type="image/jpeg")
