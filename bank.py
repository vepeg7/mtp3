"""Счёт: пополнение и снятие без ухода в минус."""

from __future__ import annotations


class BankAccount:
    def __init__(self, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError("стартовый баланс меньше нуля")
        self.balance = balance

    def deposit(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("пополнение должно быть больше нуля")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("сумма снятия должна быть больше нуля")
        if amount > self.balance:
            raise ValueError("на счёте не хватает средств")
        self.balance -= amount
        return self.balance
