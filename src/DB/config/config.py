from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
from src.DB.models.Playlist import Base

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


def connect_and_get_engine():
    engine = create_engine(f'postgresql+psycopg2://'
                           f'{os.getenv("DB_USER")}:'
                           f'{os.getenv("DB_PASSWORD")}@'
                           f'{os.getenv("DB_HOST")}:'
                           f'{os.getenv("DB_PORT")}/'
                           f'{os.getenv("DB_NAME")}')
    Base.metadata.create_all(engine)
    return engine
