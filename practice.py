
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for number in prime_numbers:
    print(f"Prime number: {number*number}")

def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(cube(n))

# a function to find simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

#create a class called Money_manager
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
    
x = MoneyManager(100000)
x.deposit(5000)
x.withdraw(10000)
print(x.get_balance())

y = MoneyManager(2000)
y.deposit(500)





