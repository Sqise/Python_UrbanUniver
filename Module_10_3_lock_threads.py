# Реализуйте программу, которая имитирует доступ к общему ресурсу
# с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами
# для пополнения и снятия денег. Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.

import random
import threading
import time


class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        print(f'Начальный баланс: ${self.balance}')
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Начислено: ${amount}. Новый баланс: ${self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Списано: ${amount}. Новый баланс: ${self.balance}")
            else:
                print(f"Недостаточно средств для списания (${amount}). Текущий баланс: ${self.balance}")


class DepositThread(threading.Thread):
    def __init__(self, account):
        super().__init__()
        self.account = account

    def run(self):
        for _ in range(5):
            amount = random.randint(100, 1000)
            self.account.deposit(amount)
            time.sleep(0.5)


class WithdrawThread(threading.Thread):
    def __init__(self, account):
        super().__init__()
        self.account = account

    def run(self):
        for _ in range(5):
            amount = random.randint(100, 1000)
            self.account.withdraw(amount)
            time.sleep(0.5)


# Создаем банковский счет с начальным балансом
account = BankAccount(1000)

# Создаем и запускаем потоки
deposit_thread = DepositThread(account)
withdraw_thread = WithdrawThread(account)

deposit_thread.start()
withdraw_thread.start()

# Ожидаем завершения потоков
deposit_thread.join()
withdraw_thread.join()
