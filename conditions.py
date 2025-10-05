
#number = int(input("enter a number: "))
"""
Input is always taken as a string. Therefore, it is important to convert it back to integer if needed.
Conversion can be doen as above or as given below in the comment.
number = int(number)
"""

# print(type(number))
# if number < 5:
#     print("Number is less than 5")
# #"elif" is supposed to be used when we have more than one condition.
# elif number < 10:
#     print("less than 10")
# #"else" should always be the last condition.
# else:
#     print("greater than 10")


#Nested if-else statements

score = int(input("Enter your score as a number:"))
activities = int(input("press 1 if part of sports, if not 0:"))

if score >= 95:
    print ("congratulations. you are eligible for the scholarship.")
elif score >=85:
    if activities ==1:
        print ("you are eligible for the scholarship")
    else:
        print("sorry, you are not eligible for the scholarship")
else:
    ("sorry, you have a very low score. therefore, you are not eligible for the scholarship.")

#Combined logic statements

scholarship = False
if score >=85 and activities == 1:
    scholarship = True
elif score >= 95:
    scholarship = True

if scholarship:
    print("You have a scholarship")
else:
    print("You dont have a scholarship")