from typing import List
import uuid
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import UUID

from src.DB.config.config import connect_and_get_engine
from src.DB.models.Media import Media
from src.DB.models.Playlist import Playlist
from sqlalchemy.orm import Session


class DAO:


    @staticmethod
    def create_playlist(chat_id: str, name: str) -> None:
        engine = connect_and_get_engine()
        with Session(engine) as session:
            playlist = Playlist(
                id=str(uuid.uuid4()),
                chat_id=chat_id,
                name=name,
            )
            session.add(playlist)
            session.commit()

    @staticmethod
    def add_media(playlist_id: UUID, link: str) -> None:
        engine = connect_and_get_engine()
        with Session(engine) as session:
            media = Media(
                playlist_id=playlist_id,
                link=link
            )
            session.add(media)
            session.commit()

    @staticmethod
    def get_playlists(chat_id: str) -> List[Playlist]:
        engine = connect_and_get_engine()
        with Session(engine) as session:
            playlists = (
                select(Playlist)
                .where(Playlist.chat_id == chat_id)
            )
            return session.scalars(playlists).all()

    @staticmethod
    def get_medias_from_playlist(playlist_id: UUID) -> List[Media]:
        engine = connect_and_get_engine()
        with Session(engine) as session:
            medias = (
                select(Media)
                .where(Media.playlist_id == playlist_id)
            )
            return session.scalars(medias).all()