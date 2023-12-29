from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
import settings
from api.handlers import user_router

app = FastAPI(title="luchanos-oxford-university")

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
