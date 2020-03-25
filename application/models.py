from sqlalchemy import Column, Integer, String, Text, DateTime
from application.database import Base

class User(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    description = Column(Text, unique=True, nullable=False)
    status = Column(String(255), unique=True, nullable=False)
    initialised = Column(DateTime, unique=True, nullable=False)

    def __init__(self, title=None, description=None, status=None, initialised=None):
        self.title = title
        self.description = description
        self.status = status
        self.initialised = initialised

    def __repr__(self):
        return '<Task %r>' % (self.title)
