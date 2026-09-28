"""Текстовый файл на диске, кодировка UTF-8."""

from __future__ import annotations

from pathlib import Path


class TextFile:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def write(self, text: str) -> None:
        self.path.write_text(text, encoding="utf-8")

    def read(self) -> str:
        return self.path.read_text(encoding="utf-8")
