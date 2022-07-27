from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Company(Base):
    __tablename__ = "Company"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    slug = Column(String, nullable=False, unique=True)
    slogan = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"{self.__name__}(id={self.id!r}, name={self.name!r})"
