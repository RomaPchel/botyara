from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.DB.models.Playlist import Base


class Media(Base):
    __tablename__ = "medias"

    id = Column(Integer, primary_key=True)
    link = Column(String(100))
    playlist_id = Column(UUID, ForeignKey("playlists.id"), nullable=False)

    def __str__(self):
        return f'ID: {self.id} link: {self.link} PLAYLIST_ID:{self.playlist_id}'

    def __repr__(self):
        return str(self)
