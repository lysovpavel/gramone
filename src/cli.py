import uuid
from asyncio import run
from datetime import datetime
from functools import wraps
from getpass import getpass
from typing import Callable

import typer

from db.base import async_session_maker
from gramone.models import AdminUser


class AsyncTyper(typer.Typer):
    def async_command(self, _func: Callable = None, *args, **kwargs):
        def decorator(async_func):
            @wraps(async_func)
            def sync_func(*_args, **_kwargs):
                return run(async_func(*_args, **_kwargs))

            self.command(*args, **kwargs)(sync_func)
            return async_func

        if _func:
            return decorator(_func)
        return decorator


cli = AsyncTyper()


@cli.async_command
async def createsuperuser():
    """Create a superuser in the application database"""
    username = typer.prompt("Enter superuser username:")
    email = typer.prompt("Enter superuser email:")
    password = getpass("Enter superuser password:")
    async with async_session_maker() as session:
        user = AdminUser(id=str(uuid.uuid4()),
                         username=username,
                         email=email,
                         hashed_password=password,
                         is_superuser=True,
                         is_active=True,
                         is_verified=True,
                         created_at=datetime.now(), )
        await user.save(session)
    typer.echo(f"Superuser with username {username} has been created")


if __name__ == "__main__":
    cli()
