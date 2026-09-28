"""Профиль: имя и город через модуль json."""

from __future__ import annotations

import json


class Profile:
    def __init__(self, name: str, city: str) -> None:
        self.name = name
        self.city = city

    def to_json(self) -> str:
        payload = {"name": self.name, "city": self.city}
        return json.dumps(payload, ensure_ascii=False)

    @classmethod
    def from_json(cls, raw: str) -> Profile:
        payload = json.loads(raw)
        return cls(name=payload["name"], city=payload["city"])
