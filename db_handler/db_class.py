from decouple import config
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from create_bot import engine

Base = declarative_base()

class UserBase(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)
    number: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self):
        return f'user(id={self.id!r}, username={self.username!r}, number={self.number!r})'

#пока добавление только для 1 строки
def add_user(username, name, lastname, number):
    with Session(engine) as session:
        user = UserBase(
            username=username,
            name=name,
            lastname=lastname,
            number=number
        )
        session.add(user)
        session.commit()
        return user.id

def fetch_users():
    with Session(engine) as session:
        stmt = select(UserBase)
        return list(session.scalars(stmt))
