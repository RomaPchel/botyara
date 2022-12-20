from sqlalchemy import create_engine

from src.DB.models.Playlist import Base


def connect_and_get_engine():
    engine = create_engine("postgresql+psycopg2://postgres:impressie@localhost:5432/CourseWork")
    Base.metadata.create_all(engine)
    return engine
