"""Демонстрация классов третьей лабораторной."""

from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

from bank import BankAccount
from counter import Counter
from files import TextFile
from json_codec import Profile
from orm import MiniTable


def main() -> None:
    left = Counter(2)
    right = Counter(5)
    total = left + right
    print(f"счётчики: {left.value} + {right.value} = {total.value}")
    print(f"после up у левого: {left.up()}")
    print(f"правый не изменился: {right.value}")

    with tempfile.TemporaryDirectory(prefix="mtp3-note-") as folder:
        note = TextFile(Path(folder) / "note.txt")
        note.write("черновик к паре")
        print(f"из файла: {note.read()}")

    wallet = BankAccount(80)
    wallet.deposit(20)
    wallet.withdraw(15)
    print(f"баланс: {wallet.balance}")

    connection = sqlite3.connect(":memory:")
    shelf = MiniTable(connection)
    shelf.insert({"title": "блокнот", "qty": 6})
    print(f"таблица: {shelf.select_all()}")

    card = Profile("Егор", "Калуга")
    packed = card.to_json()
    restored = Profile.from_json(packed)
    print(f"json круг: {restored.name}, {restored.city}")


if __name__ == "__main__":
    main()
