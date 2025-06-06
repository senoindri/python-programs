#Q3. Which Python statements are used to catch and handle exceptions? Explain with an example.
#A. the keyword used to catch and exception is try, and to handle it is except. the statements that mights generate an error are places in the try block. here, in case an exception arises, it sends the control to the respective except block. the except block 'catches' the exception and prints a proper error message. 

try:
    print(10/0)
except ZeroDivisionError as e:
    print('cant help due to ',e)