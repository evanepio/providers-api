from faker import Faker
from slugify import slugify
from sqlalchemy import create_engine, select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Company

engine: Engine = create_engine("sqlite+pysqlite:///my.db", echo=True, future=True)


SessionLocal = sessionmaker(bind=engine)


Base.metadata.create_all(engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def main():
    print("Starting...")

    fake = Faker()

    session = next(get_db())
    for _ in range(100):
        name = fake.unique.company()
        values = {
            "name": name,
            "slug": slugify(name),
            "slogan": fake.unique.catch_phrase(),
        }
        session.execute(insert(Company).values(**values).on_conflict_do_nothing())

    session.commit()

    companies = session.execute(select(Company))
    for company in companies:
        print(f"{company.Company.name}: {company.Company.slogan}")


if __name__ == "__main__":
    main()
