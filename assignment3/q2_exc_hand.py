#Q2. What happens when an exception is not handled? Explain with an example.
#A. when an exception is not handled, the program may crash. it will halt abruptly where the unhandled exception occurs, and then it terminates and no program execution beyond that point occurs. 

print(10/0)
print('hello')

#10/0 results in a ZeroDivisionError and since this exception is not handled, it stops execution and print('hello') line after that is not executed
