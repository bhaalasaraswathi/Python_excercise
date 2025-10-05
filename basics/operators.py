name = 'Harini'
age = 27
is_student = True

x = 10 #x is an integer
y = 3.14 #y is a float (decimal number)
z = 'Hello' # z is a string

print ("before x =", x)
print ("before x =", type (x))

x = 'now i am a string'
print ("x =", x)
print ("x = ", type (x))

# This is a single line comment
"""
This is a 
Multiline comment.
It helps me write as much comment as i want
"""

""" This is a basic code to explain how input function works in python
this code will take input from user and print it on the screen """

# # taking input from the user
# input_data = input("enter your name: ")


# # printing the input data
# print (" Hello", input_data, "nice to meet you.....")

#OPERATORS

#arithematic operatos
# a = 10
# b = 9
# print ( "addition a + b =", a+b)
# print ( "subtraction a - b =", a-b)
# print ("multiplication a*b =", a*b)
# print (f"multiplication a*b ={a*b} Km/s")
# print ("Division a/b =", a/b)
# print (r"Reminder a % b =", a%b)
# print ("Exponent a**b =", a**b)
# print ("floor division a/b =", a/b)


# #COMPARISON OPERATORS
# x=10
# y=25
# print (f"equal to - {x==y}")
# print (f"not equal to - {x!=y}")
# print (f"greater than - {x>y}")
# print (f"less than - {x<y}")
# print (f"greater than or equal to - {x>=y}")
# print (f"less than or equal to - {x<=y}")

#LOGIC OPERATORS
"""
Condition1 AND Condition2 = True if both conditions are true
Condition1 OR Condition2 = True if atleast one condition is true
NOT Condition1 = True if  condition is false
NOT Condition2 = True if  condition is false
"""

user_age = 20
country = "India"
if user_age >=18 and country == "India":
    print("You are elegible to vote")
else:
    print("You are not eligible to vote")


#BITWISE OPERATORS
"""They work in binary numbers. they help in advanced operations 
&:AND
|:OR
~:NOT
"""
#5 = 0101
#3 = 0011
#5&3 = 0101
a=5
b=3
print(f"bitwise AND - {a&b}")
print(f"bitwise OR - {a|b}")
