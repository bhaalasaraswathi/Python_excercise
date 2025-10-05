def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

class MoneyManager:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    manager = MoneyManager(1000)
    print("Initial Balance:", manager.get_balance())
    manager.deposit(500)
    print("After Deposit:", manager.get_balance())
    manager.withdraw(200)
    print("After Withdrawal:", manager.get_balance())
    interest = simple_interest(1000, 5, 2)
    print("Simple Interest on 1000 at 5% for 2 years:", interest)