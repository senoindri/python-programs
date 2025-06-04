#Q14. Implement a decorator @log_calls to log the name and arguments of any function called.
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

@log_calls
def add(a, b):
    return a + b

greet("Oindri")
greet("Amiya", message="Good morning") #explicitly overriding
print("Sum:", add(5, 7))