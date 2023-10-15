import os
from sqlalchemy import create_engine, MetaData, Table, Column, String


def create_students_table():
    database_url = os.getenv("DATABASE_URL")

    engine = create_engine(database_url)
    metadata = MetaData()

    Table(
        "students",
        metadata,
        Column("name", String),
        Column("course", String),
        Column("year", String),
    )

    metadata.create_all(engine)


if __name__ == "__main__":
    create_students_table()