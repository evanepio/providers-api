from faker import Faker
from slugify import slugify
from sqlmodel import Session, SQLModel, create_engine

from .models import Company

engine = create_engine("sqlite+pysqlite:///my.db", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


def init_db():
    print("Starting...")

    fake = Faker()

    session = Session(engine)
    # session = next(get_db())
    for _ in range(100):
        name = fake.unique.company()
        session.add(
            Company(
                name=name,
                slug=slugify(name),
                slogan=fake.unique.catch_phrase(),
            )
        )

    session.commit()
    session.close()


if __name__ == "__main__":
    create_db_and_tables()
