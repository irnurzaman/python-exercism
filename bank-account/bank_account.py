import threading


class BankAccount:
    def __init__(self):
        self.status = False
        self.balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        if self.status is False:
            raise ValueError('Account is alread closed!')
        return self.balance

    def open(self):
        if self.status is True:
            raise ValueError("Account is already opened!")
        self.status = True

    def deposit(self, amount):
        self.lock.acquire()
        if self.status is False:
            raise ValueError("Account is already closed")
        if amount < 0:
            raise ValueError("Invalid deposit amount!")
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        if self.status is False:
            raise ValueError("Account is already closed")
        if amount < 0:
            raise ValueError("Invalid withdraw amount!")
        if amount > self.balance:
            raise ValueError("Can't withdraw excess balance")
        self.balance -= amount
        self.lock.release()

    def close(self):
        if self.status is False:
            raise ValueError("Account is already closed!")
        self.status = False
        self.balance = 0
