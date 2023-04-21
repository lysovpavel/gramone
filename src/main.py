import asyncio

import uvicorn
from aiogram.utils import executor

from bot.main import dp
from gramone.admin import admin  # noqa
from gramone.app import app

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # config = uvicorn.Config(app=app, port=8080, loop=loop)
    config = uvicorn.Config(app=app, port=8080)
    server = uvicorn.Server(config)
    # loop.run_until_complete(server.serve())
    asyncio.ensure_future(server.serve())
    executor.start_polling(dp, skip_updates=True)
