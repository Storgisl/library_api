from ..base import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    publication_date = Column(Date, nullable=False)
    available_copies = Column(Integer, default=0)

    # ForeignKey for the author (One-to-Many relationship)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="books")

    # Many-to-Many relationship with genres
    genres = relationship(
        "Genre", secondary=book_genre_association, back_populates="books"
    )
