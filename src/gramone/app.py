from fastapi import FastAPI

from gramone.views.message import message_router

app = FastAPI()

app.include_router(message_router, prefix="/api/v1", tags=["messages"])
