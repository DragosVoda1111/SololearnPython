#EXCEPTIONS

"""Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
"""


#Exception Handling

"""To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. If no error occurs, the code in the except block doesn't run.
For example:"""




try:
    num1=7
    num2=0
    print(num1/num2)
    print("done caculation")
except ZeroDivisionError:            #In this code, the except statement defines the type of exception to handle (in our case, the ZeroDivisionError).
    print("an error occured")
    print("due to zero division")




"""A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
"""


try:
    variable = 10
    print(variable+ "hello")
    print(variable/2)
except ZeroDivisionError:
    print("divided by zero")
except (ValueError, TypeError):
    print("error occurred")




"""To ensure some code runs no matter what errors occur, you can use a finally statement. 
The finally statement is placed at the bottom of a try/except statement. 
Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks."""

try:
    print("hello")
    print(1/0)
except ZeroDivisionError:
    print("divided by zero")
finally:
    print("this code will run no matter what")




#RAISING EXCEPTIONS

"""Exceptions can be raised with arguments that give detail about them.
For example:"""


#name = "123"
#raise NameError("invalid name!")


"""In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
For example:"""


try:
    num = 5/0
except:
    print("an error occured")
    raise