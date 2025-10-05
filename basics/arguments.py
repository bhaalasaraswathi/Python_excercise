
import sys
from money import simple_interest
from money import MoneyManager


#take parameters from command line
if len(sys.argv) != 4:
    print("Usage: python arguments.py <principal> <rate> <time>")
    sys.exit(1)

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])
print(simple_interest(principal, rate, time))

#use principal as the initial amount in MoneyManager class
manager = MoneyManager(principal)
print(manager.get_balance())

#deposit the simple interest amount
interest = simple_interest(principal, rate, time)
manager.deposit(interest)
print(manager.get_balance())
