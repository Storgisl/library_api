from sqlalchemy import Column, Integer, String, Text
from ..base import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    biography = Column(Text, nullable=True)

    # One-to-Many: An author can have multiple books
    books = relationship("Book", back_populates="author")
