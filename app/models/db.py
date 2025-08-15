"""

"""
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Enum as SQLAlchemyEnum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import List

db = SQLAlchemy()

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

class Conversation(Base):
    __tablename__ = 'conversations'
    id: Mapped[int] = mapped_column(primary_key=True)
    messageid: Mapped[int] = mapped_column(Integer)
    to: Mapped[str] = mapped_column(String, nullable=False)
    frm: Mapped[str] = mapped_column('from', String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    threadcode: Mapped[str] = mapped_column(String, nullable=False)