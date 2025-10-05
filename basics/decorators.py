def decorator(func):
    def wrapper(*args):
        print("Decorator is called")
        result =func(*args)
        print("Decorator is finished")
        return result
    return wrapper


@decorator
def division(a,b):
    print("Division function is called", a/b, a//b, a%b)
    return [a/b, a//b, a%b]

print(division(5,2))

@decorator
def square(x):
    print("Square function is called", x*x)
    return x*x
print(square(5))