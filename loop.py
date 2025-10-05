# loops are functions that can be used to repeat a line of code continuously

#"for loops" (used when we know the defenite number of iterations)
# shopping_list = [ 'apple', 'mango', 'banana', 'orange', 'guava', 'jackfruit']

# for item in shopping_list:
#     print (item)

# #range function. by default, the range function is taken to be 1. this can be changed to suit our required need.
# for item in range(1,12):
#     print(item)

#the last number indicates the steps(intervals b/w the numbers)
# for item in range(1,12,3):
#     print(item)

#"while loops" (used when we do not know the defenite number of iterations)
#when using "while loops", remeber to use a stop statement. this is very imp. 
# if not the code will change to an infinite loop and kepp printing it forever.

# count = 0

# while count < 5:
#     print(count)
#     count +=1

"""
# Loop control statements
break = exits the loop immedieately
continue = skips the current iteration and moves to the next.
pass = place holder, does nothing.
"""

for number in range(1,10):
    if number == 5:
        print ("breaking the loop at 5.")
        break #exit the loop when the number is 5
    if number % 2 == 0:
        print ("skipping an even number.")
        continue # skip even numbers
    print (f"Number: {number}")
