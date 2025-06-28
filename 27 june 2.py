class ATM:
    def __init__(self, balance=0, pin="0000"):
        self.balance = balance
        self.pin = pin
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            self.transactions.append("PIN Changed")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    def transaction_failed(self, reason):
        self.transactions.append(f"Transaction Failed: {reason}")
        return False