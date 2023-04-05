from datetime import datetime
from dataclasses import dataclass


history = []


class Bank:

    def __init__(self):
        self.balance = 0

    @property
    def balance_account(self):
        return self.balance

    @balance_account.setter
    def balance_account(self, refill: int):
        self.balance += refill
        time_ = datetime.now()
        if refill > 0:
            history.append(f"Пополнение баланса на: {refill},время пополнения: "
                            f"{time_} текущий баланс: {self.balance}")
        else:
            history.append(f"Снятие со счета в размере: {refill},время снятия: "
                            f"{time_} текущий баланс: {self.balance}")
        print(f"Текущий баланс: {self.balance}")
        print(history)


account = Bank()
account.balance_account = 100
account.balance_account = -100
account.balance_account = 500


