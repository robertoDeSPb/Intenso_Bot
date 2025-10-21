from decouple import config
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import select
from create_bot import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    number = Column(Integer, primary_key=False)

    def __repr__(self):
        return f'user(id={self.id!r}, username={self.username!r}, number={self.number!r})'

#пока добавление только для 1 строки
def insert_into(tg_user: User):
    with Session(engine) as session:
        session.add(User)
        session.commit()

def select_from(stmt):
    with Session(engine) as session:
        return [row for row in session.scalars(stmt)]
  