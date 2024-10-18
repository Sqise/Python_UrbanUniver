from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.backend.db import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    title = Column(String, index=True)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    #user_id = Column(Integer, ForeignKey('users.id', nullable=False), index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="tasks")


print(CreateTable(Task.__table__))
