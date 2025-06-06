#Q2. Write a python program to print Python Exception Hierarchy.
def print_exception_tree(cls, indent=0):
    print(' ' * indent + cls.__name__)
    for subclass in cls.__subclasses__():
        print_exception_tree(subclass, indent + 4)

# Start from the base exception class
print("\nPython Exception Hierarchy:\n")
print_exception_tree(BaseException)