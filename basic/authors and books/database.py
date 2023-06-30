from sqlalchemy .ext. declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, column, create_engine
from datetime import datetime

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    Created_date = Column(DateTime, default=datetime.now)

    def __str__(self):
         return self.name

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    publication = Column(String(50))
    pages = Column(Integer)
    auther_id = Column(Integer, ForeignKey('authors.id'))
    created_date = Column(DateTime, default=datetime.now)

    def __str__ (self):
        return self.title

if __name__ == '__main__':
    engine = create_engine('sqlite:///mydb.sqlite', echo=True)
    Base.metadata.create_all(engine)