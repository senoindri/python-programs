#Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.
#A. the errors defined in the Arithmetic errors class are FloatingPointError, OverflowError, ZeroDivisionError
import math
try:
    print(math.exp(1000))
except OverflowError as e:
    print('so',e)

try:
    print(10/0)
except ZeroDivisionError as e:
    print('also',e)