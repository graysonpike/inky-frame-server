from fastapi import FastAPI
from api.routers import testing


openapi_metadata = [
    testing.openapi_metadata
]

app = FastAPI(
    openapi_tags=openapi_metadata
)

app.include_router(testing.router, tags=["Testing"])
