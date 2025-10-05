"""
functions helps us code once and reuse it multiple times.
functions improve code oragnisation and reusability.
it is 
modular - break code into reuseable parts
maintainable - easier to update and debug
effecient - saves time and reduces effort. 
"""

def details_input(Name="ganesha", Age=33):
    y = "func local"
    return f"My name is {Name}, I'm {Age} years old."

print(details_input())
m = "Aravind"
print(details_input(Name=m, Age=33))

"""
#function syntax
def function_name(parameters):
    #code block
    return value
"""
num = [1,2,3,4,5,6]
def square(number):
    # y = number*number
    # return y
    return number*number

#calling the function
for bb in num:
    print (square(bb))

def greet(name):
    return f"hello, {name}"

print (greet("alice"))
print (greet("bob"))

#parameter = place holder
#argument = actual value

#providing default values to parameters

def coffee(sugar="1tsp", milk="200ml"):
    return f"coffe with {sugar} sugar and {milk} milk"


def coffee2(sugar="1tsp", milk="200ml"):
    print(f"coffe with {sugar} sugar and {milk} milk")

a = coffee2()
print(f"A is {a}")

a = coffee()
print(f"A is {a}")

print(coffee())
print(coffee(sugar="1/2tsp"))
print(coffee(milk="250ml"))


#(*args) function
#this helps us give undefined amount of arguments to the function
# def sum(args):
#     sum = 0
#     for x in args:
#         sum = sum + x
#     return sum

def add(*args):
    square = 0
    for x in args:
        square = square + x*x
    return square

y = add(1,2,4,6)
print(y)

def something(**x):
    print(x)

something(sugar="1tsp", milk=2, elaka="2 tbsp")


#(*kwargs)function
#this function helps ud give values(=) to the variours arguments in the parameter

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="alice", age=25, city="new york")
display_info(name="bob", age=55, city="pittsburg")

"""
Scope and lifetime of variables
There are 2 types of variables. 
1. local variables = defined inside a function
2. global variabales = defeined outside in the golbal space. called inside a function to make changes to it.
then you have to use the keyword "global"
"""

#global variable example
count = 0
def increment():
    global count
    print(count, "This is from inside the function")
    count = count + 1 # This can also be written as "count =+ 1"
increment()
print(count, "This is from outside the function")
