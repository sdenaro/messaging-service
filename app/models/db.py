"""

"""
import datetime
import config as Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, create_engine, text
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import List
from app import db

uuid_query = """

"""

class Base(DeclarativeBase):
    pass

class Attachment(Base):
    __tablename__ = 'attachments'
    id: Mapped[int] = mapped_column(primary_key=True)
    message_id: Mapped[int] = mapped_column(db.ForeignKey('messages.id'))
    url: Mapped[str] = mapped_column(String, nullable=False)
    message: Mapped["Message"] = relationship(back_populates="attachments")

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    frm: Mapped[str] = mapped_column('from', String, nullable=False)
    to: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False) 
    body: Mapped[str] = mapped_column(String, nullable=False)
    xillio_id: Mapped[str] = mapped_column(String, nullable=True)
    attachments: Mapped[List["Attachment"] | None ] = relationship(
        back_populates="message", cascade="all, delete-orphan"
    )
    timestamp: Mapped[str] = mapped_column(String, nullable=False)
#    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)

class Conversation(Base):
    __tablename__ = 'conversations'
    id: Mapped[int] = mapped_column(primary_key=True)
    to: Mapped[str] = mapped_column(String, nullable=False)
    frm: Mapped[str] = mapped_column('from', String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    threadcode: Mapped[str] = mapped_column(String, nullable=False)

def check_for_thread(to:str, frm:str) -> str:
    
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

    with engine.connect() as connection:
    
        result = connection.execute(uuid_query, 
            {"to_param": to_user, "from_param": from_user})
            
        # .scalar_one_or_none() is useful for fetching a single value from a
        # query that is expected to return at most one row.
        
        found_uuid = result.scalar_one_or_none()

        if found_uuid:
            print(f"✔️ Found Message UUID: {found_uuid}")
        else:
            print("🔸 No matching message found.")

        return found_uuid



