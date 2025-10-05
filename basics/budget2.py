class Budget:
    # x = Budget(total_money=4000, rent=1000, groceries=0.40, utilities=0.30, savings=0.30) 
    def __init__(self, total_money, rent, groceries, utilities, savings):
        self.total_money = total_money
        
        self.rent_budget = rent
        availble_money = total_money - rent
        self.groceries_budget = availble_money * groceries
        self.utilities_budget = availble_money * utilities
        self.savings_budget = availble_money * savings


bd = Budget(total_money=4500, rent=1100, groceries=0.25, utilities=0.25, savings=0.50)
print(f"Rent Budget: {bd.rent_budget}")
print(f"Groceries Budget: {bd.groceries_budget}")
print(f"Utilities Budget: {bd.utilities_budget}")
print(f"Savings Budget: {bd.savings_budget}")
