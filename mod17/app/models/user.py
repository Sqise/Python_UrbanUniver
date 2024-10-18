from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.backend.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="user")

print(CreateTable(User.__table__))