from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.mount("/images", StaticFiles(directory="images"), name="images")

# Set all CORS enabled origins
# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],

@app.get("/")
async def root():
    return {"message":"Hello World"}
    
app.include_router(api_router, prefix=settings.API_V1_STR)