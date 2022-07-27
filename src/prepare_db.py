from faker import Faker
from slugify import slugify
from sqlalchemy import create_engine, insert
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from db.models import Base, Company


def main():
    print("Starting...")
    
    Base.metadata.create_all(create_engine("sqlite+pysqlite:///my.db", future=True))

    engine: Engine = create_engine("sqlite+pysqlite:///my.db", echo=True, future=True)

    fake = Faker()

    with Session(engine) as session:
        for _ in range(100):
            name = fake.unique.name()
            values = {
                'name': name,
                'slug': slugify(name),
                'slogan': fake.unique.catch_phrase()
            }
            session.execute(insert(Company).values(**values))


if __name__ == "__main__":
    main()