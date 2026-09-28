"""Счётчик с шагом вверх, вниз и сложением."""

from __future__ import annotations


class Counter:
    def __init__(self, value: int = 0) -> None:
        self.value = value

    def up(self, step: int = 1) -> int:
        self.value += step
        return self.value

    def down(self, step: int = 1) -> int:
        self.value -= step
        return self.value

    def __add__(self, other: Counter) -> Counter:
        # Новый экземпляр: чужие value не переписываем.
        if not isinstance(other, Counter):
            return NotImplemented
        return Counter(self.value + other.value)
