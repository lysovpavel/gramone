import asyncio

from aiogram.utils.executor import Executor
from fastapi import FastAPI

from gramone.views.message import message_router

app = FastAPI()


# @app.on_event("startup")
# async def startup_event():
#     from bot.main import dp
#     executor = Executor(dp, skip_updates=True)
#     asyncio.ensure_future(executor._startup_polling())
#     asyncio.ensure_future(executor.dispatcher.start_polling(reset_webhook=True, timeout=20, relax=0.1, fast=True,
#                                                             allowed_updates=None))


app.include_router(message_router, prefix="/api/v1", tags=["messages"])
