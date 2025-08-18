from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models.db import Base, Message, Attachment, check_for_thread
from config import Config
import uuid

# Create the SQLAlchemy engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


# Test the connection and then clean up existing tables
try:
    with engine.connect() as connection:
        print("Successfully connected to the PostgreSQL database!")
        connection.execute(text("DROP TABLE IF EXISTS public.attachments"))
        connection.execute(text("DROP TABLE IF EXISTS public.conversations"))
        connection.execute(text("DROP TABLE IF EXISTS public.messages"))
except Exception as ex:
    print(f"Failed to connect: {ex}")

# Create the tables based on objects
Base.metadata.bind = engine
Base.metadata.create_all(engine)

#Force creation
Session = sessionmaker(bind=engine)
session = Session()

def uuid_check(to_user:str, from_user:str) -> str:
    message = session.execute(Message.__table__.select().where(Message.frm==to_user and Message.to==from_user)).first()

    if message:
        return message.threadcode
    else:
        return uuid.uuid4()


### SMS

# Query for User objects
#statement = select(Conversation).filter_by(name='Alice')


# no attachment
sms = Message(frm="+11111111111", to="+22222222222", type="SMS", body="test", timestamp="timestamp", threadcode=uuid.uuid4())
session.add(sms)
session.commit()

#conversation = Conversation(messageid=1, to="+22222222222", frm="+11111111111", created_at="2025-08-15 12:00:00", threadcode="threadcode")
#session.add(conversation)

# one attachment

sms1 = Message(frm="+22222222222", to="+11111111111", type="SMS", body="test", timestamp="timestamp", attachments=[Attachment(url="https://xyx.com/foo.jpg"  )])
sms1.threadcode = uuid_check(sms1.to,sms1.frm)

i = session.add(sms1)


#    user = session.execute(User.__table__.select().where(User.name == 'Alice')).first()

#m2 = session.execute(Message.__table__.select().where(Message.frm==sms1.to and Message.to==sms1.frm)).first()

uuid_text = uuid_check(sms1.to,sms1.frm)
print("thread found")
print(uuid_text)

# two attachments

#at2 = Attachment(url="https://xyx.com/foo.jpg"  )
#at3 = Attachment(url="https://abc.com/bar.jpg"  )


sms2 = Message(frm="+11111111111", to="+22222222222", type="SMS", body="test",   timestamp="timestamp", attachments=[Attachment(url="https://xyx.com/foo2.jpg"  ), Attachment(url="https://abc.com/bar.jpg"  ) ])
sms2.threadcode = uuid_check(sms2.to,sms2.frm)

i = session.add(sms2)


### email


#SELECT c.*
#FROM
#    conversations c
#WHERE EXISTS (
#    SELECT 1
#    FROM messages m
#    WHERE
#        (c.to = m.to AND c.frm = m.frm) OR
#        (c.to = m.frm AND c.frm = m.to)
#);


#email = Message(frm="[user@usehatchapp.com](mailto:user@usehatchapp.com)", to="[contact@gmail.com](mailto:contact@gmail.com)", body="test1", timestamp="timestamp",  type="email",  xillio_id="xillio_id  1")
#session.add(email)

#email2 = Message(to="[user@usehatchapp.com](mailto:user@usehatchapp.com)", frm="[contact@gmail.com](mailto:contact@gmail.com)", body="test2", timestamp="timestamp",  type="email", xillio_id="xillio_id  1", attachments=[Attachment(url="https://meow.com/cat.jpg"  )])
#session.add(email2)

#email3 = Message(frm="[user@usehatchapp.com](mailto:user@usehatchapp.com)", to="[contact@gmail.com](mailto:contact@gmail.com)", body="test3", timestamp="timestamp",  type="email", xillio_id="xillio_id  1")
#session.add(email3)


# no attachment

# one attachment

# two attachments


session.commit()
