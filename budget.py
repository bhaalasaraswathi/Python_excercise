class Budget:
    def __init__(self, groceries, education, rent, utilities, miscellaneous=6000):
        self.limit_groceries = groceries
        self.limit_education = education
        self.limit_rent = rent
        self.limit_utilities = utilities
        self.limit_miscellaneous = miscellaneous

    def register_groceries(self, amount):
        if amount > self.limit_groceries:
            print("Expense exceeds groceries budget limit.")
            return False
        else:
            self.limit_groceries -= amount
            print(f"Registered groceries expense of {amount}. Remaining groceries budget: {self.limit_groceries}")
            return True
    def register_education(self, amount):
        if amount > self.limit_education:
            print("Expense exceeds education budget limit.")
            return False
        else:
            self.limit_education -= amount
            print(f"Registered education expense of {amount}. Remaining education budget: {self.limit_education}")
            return True
    def register_rent(self, amount):
        if amount > self.limit_rent:
            print("Expense exceeds rent budget limit.")
            return False
        else:
            self.limit_rent -= amount
            print(f"Registered rent expense of {amount}. Remaining rent budget: {self.limit_rent}")
            return True
    def register_utilities(self, amount):
        if amount > self.limit_utilities:
            print("Expense exceeds utilities budget limit.")
            return False
        else:
            self.limit_utilities -= amount
            print(f"Registered utilities expense of {amount}. Remaining utilities budget: {self.limit_utilities}")
            return True
    def register_miscellaneous(self, amount):
        if amount > self.limit_miscellaneous:
            print("Expense exceeds miscellaneous budget limit.")
            return False
        else:
            self.limit_miscellaneous -= amount
            print(f"Registered miscellaneous expense of {amount}. Remaining miscellaneous budget: {self.limit_miscellaneous}")
            return True
        
x=Budget(education=5000, groceries=2000, rent=15000, utilities=3000)
if x.register_groceries(500) == True:
    print("Expense registered successfully.")
else:
    print("Failed to register expense.")


