from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import as_declarative, declared_attr, sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost/library"

# Create engine, session, and Base
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
