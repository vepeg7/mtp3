"""Тонкая обёртка над одной таблицей sqlite."""

from __future__ import annotations

import sqlite3


class MiniTable:
    def __init__(self, conn: sqlite3.Connection, name: str = "items") -> None:
        if not name.isidentifier():
            raise ValueError("имя таблицы не идентификатор")
        self._conn = conn
        self._name = name
        self._conn.execute(
            f"CREATE TABLE IF NOT EXISTS {name} ("
            "id INTEGER PRIMARY KEY, title TEXT, qty INTEGER)"
        )
        self._conn.commit()

    def insert(self, row: dict) -> dict:
        cursor = self._conn.execute(
            f"INSERT INTO {self._name} (title, qty) VALUES (?, ?)",
            (row["title"], row["qty"]),
        )
        self._conn.commit()
        return {"id": cursor.lastrowid, "title": row["title"], "qty": row["qty"]}

    def select_all(self) -> list[dict]:
        cursor = self._conn.execute(
            f"SELECT id, title, qty FROM {self._name} ORDER BY id"
        )
        found: list[dict] = []
        for row_id, title, qty in cursor.fetchall():
            found.append({"id": row_id, "title": title, "qty": qty})
        return found
