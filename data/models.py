import sqlite3

from config import DATABASE_PATH


def initialize_database() -> None:
    try:
        connection = sqlite3.connect(
            DATABASE_PATH
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS saved_plans (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL
            )
            """
        )

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"SQLite no pudo iniciar: {error}"
        ) from error


def save_plan(title: str) -> None:
    if not title:
        raise RuntimeError(
            "No puedes guardar un plan vacío."
        )

    try:
        connection = sqlite3.connect(
            DATABASE_PATH
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO saved_plans (title)
            VALUES (?)
            """,
            (title,),
        )

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        raise RuntimeError(
            f"SQLite no pudo guardar el plan: {error}"
        ) from error
