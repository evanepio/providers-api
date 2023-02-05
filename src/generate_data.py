from faker import Faker
from slugify import slugify
import httpx

from providers.db.core import create_db_and_tables


def insert_random_stuff():
    print("Starting...")

    fake = Faker()

    for _ in range(100):
        name = fake.unique.company()
        data = {
            "name": name,
            "slug": slugify(name),
            "slogan": fake.unique.catch_phrase(),
        }
        response = httpx.post("http://127.0.0.1:8000/companies/", json=data)

        print(response.headers)


if __name__ == "__main__":
    create_db_and_tables()
    insert_random_stuff()
