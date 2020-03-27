from sqlalchemy import Column, Integer, String, Text, DateTime
from application.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(255), nullable=False)
    initialised = Column(DateTime, nullable=False)

    def __init__(self, title=None, description=None, status=None, initialised=None):
        self.title = title
        self.description = description
        self.status = status
        self.initialised = initialised

    def __repr__(self):
        return '<Task %r>' % (self.id)
