from sqlmodel import Session, SQLModel, create_engine

engine = create_engine("sqlite+pysqlite:///my.db", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
