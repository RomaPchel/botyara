from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, backref
from sqlalchemy.orm import relationship

Base = declarative_base()


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(UUID, primary_key=True)
    name = Column(String(30))
    chat_id = Column(String)
    media = relationship(
        "Media", cascade="all, delete-orphan", backref=backref('voteinfo', uselist=False)
    )

    def __str__(self):
        return f'ID: {self.id} {self.name} {self.media}'



