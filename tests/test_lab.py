"""Проверки лабораторной №3."""

from __future__ import annotations

import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from bank import BankAccount
from counter import Counter
from files import TextFile
from json_codec import Profile
from orm import MiniTable

_ROOT = Path(__file__).resolve().parents[1]


def test_counter_steps_and_sum() -> None:
    counter = Counter()
    assert counter.up() == 1
    assert counter.up(4) == 5
    assert counter.down(2) == 3
    first = Counter(2)
    second = Counter(5)
    merged = first + second
    assert merged.value == 7
    assert first.value == 2
    assert second.value == 5


def test_text_file_roundtrip(tmp_path: Path) -> None:
    target = TextFile(tmp_path / "note.txt")
    target.write("строка для диска")
    assert target.read() == "строка для диска"


def test_bank_account() -> None:
    account = BankAccount(10)
    assert account.deposit(5) == 15
    assert account.withdraw(4) == 11
    with pytest.raises(ValueError):
        account.withdraw(40)
    assert account.balance == 11
    with pytest.raises(ValueError):
        account.withdraw(0)
    assert account.balance == 11
    with pytest.raises(ValueError):
        BankAccount(-1)


def test_mini_table_insert_select() -> None:
    connection = sqlite3.connect(":memory:")
    table = MiniTable(connection)
    stored = table.insert({"title": "альбом", "qty": 2})
    assert stored["title"] == "альбом"
    assert stored["qty"] == 2
    rows = table.select_all()
    assert rows[0]["title"] == "альбом"
    assert rows[0]["qty"] == 2
    assert rows[0]["id"] == stored["id"]


def test_profile_json_roundtrip() -> None:
    source = Profile("Егор", "Орёл")
    restored = Profile.from_json(source.to_json())
    assert restored.name == "Егор"
    assert restored.city == "Орёл"


def test_main_cli() -> None:
    completed = subprocess.run(
        [sys.executable, "main.py"],
        cwd=_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
