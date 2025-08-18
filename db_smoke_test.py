from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models.db import db, Base, Message, Attachment, Conversation
from config import Config

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

### SMS

# Query for User objects
#statement = select(Conversation).filter_by(name='Alice')


# no attachment
sms = Message(frm="+11111111111", to="+22222222222", type="SMS", body="test", timestamp="timestamp")
session.add(sms)

#conversation = Conversation(messageid=1, to="+22222222222", frm="+11111111111", created_at="2025-08-15 12:00:00", threadcode="threadcode")
#session.add(conversation)

# one attachment

sms1 = Message(frm="+22222222222", to="+11111111111", type="SMS", body="test", timestamp="timestamp", attachments=[Attachment(url="https://xyx.com/foo.jpg"  )])
i = session.add(sms1)


# two attachments

#at2 = Attachment(url="https://xyx.com/foo.jpg"  )
#at3 = Attachment(url="https://abc.com/bar.jpg"  )


sms2 = Message(frm="+11111111111", to="+22222222222", type="SMS", body="test", timestamp="timestamp", attachments=[Attachment(url="https://xyx.com/foo2.jpg"  ), Attachment(url="https://abc.com/bar.jpg"  ) ])
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


email = Message(frm="[user@usehatchapp.com](mailto:user@usehatchapp.com)", to="[contact@gmail.com](mailto:contact@gmail.com)", body="test1", timestamp="timestamp",  type="email",  xillio_id="xillio_id  1")
session.add(email)

email2 = Message(to="[user@usehatchapp.com](mailto:user@usehatchapp.com)", frm="[contact@gmail.com](mailto:contact@gmail.com)", body="test2", timestamp="timestamp",  type="email", xillio_id="xillio_id  1", attachments=[Attachment(url="https://meow.com/cat.jpg"  )])
session.add(email2)

email3 = Message(frm="[user@usehatchapp.com](mailto:user@usehatchapp.com)", to="[contact@gmail.com](mailto:contact@gmail.com)", body="test3", timestamp="timestamp",  type="email", xillio_id="xillio_id  1")
session.add(email3)


# no attachment

# one attachment

# two attachments


session.commit()
