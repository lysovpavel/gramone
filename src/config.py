import os

from dotenv import load_dotenv

load_dotenv()

DB = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
