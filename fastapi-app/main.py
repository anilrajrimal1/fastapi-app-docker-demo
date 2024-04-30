from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/")
async def root():
    return {"message": "Hi"}