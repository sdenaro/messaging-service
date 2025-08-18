"""

"""
import datetime
import uuid
import config as Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, select, text
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import List
from app import db

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
    threadcode: Mapped[str] = mapped_column(String, nullable=False)
    messaging_provider_id: Mapped[str] = mapped_column(String, nullable=True)
    xillio_id: Mapped[str] = mapped_column(String, nullable=True)
    attachments: Mapped[List["Attachment"] | None ] = relationship(
        back_populates="message", cascade="all, delete-orphan"
    )
    timestamp: Mapped[str] = mapped_column(String, nullable=False)
#    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)

def threads():
    
    threads_list = db.session.query(Message.threadcode).distinct().all()

    return [threadcode[0] for threadcode in threads_list]

def conversation(uuid:str) -> List[Message]:
    """
    return list of messages for uuid
    """
    return db.session.execute(Message.__table__.select().where(Message.threadcode==uuid)).all()

def check_for_thread(to_user:str, from_user:str) -> str:
    """
    check for a thread code by looking for prior message with to and from reversed
    if not, create a uuid
    """
    message = db.session.execute(Message.__table__.select().where(Message.frm==to_user and Message.to==from_user)).first()

    if message:
        return message.threadcode
    else:
        return uuid.uuid4()
