#MAKING YOUR OWN FUNCTIONS


def myfunc():
    print("spam")
    print("spam")
    print("spam")

myfunc()




def hello():
    print("Hello world!")

hello()
hello()
hello()




#Functions can take arguments, which can be used to generate the function output.
#For example:


def printex (word):
    print(word + "!")

printex("spam")
printex("eggs")
printex("python")




def print_double(x):
    print(2*x)

print_double(3)






#Even better, you can define functions with more than one argument; separate them with commas. Like this:




def print_sum_twice(x,y):
    print(x + y)
    print(x+y)

print_sum_twice(5,8)




#RETURNING FROM FUNCTIONS

"""Certain functions, such as int or str, return a value instead of outputting it.

The returned value can be used later in the code, for example, by getting assigned to a variable.

To do this for your defined functions, you can use the return statement. Like this:
For example:
"""

def min(x,y):
    if x<=y:
        return x
    else:
        return y

print(min(5,6))





def max(x,y):
    if x>=y:
        return x
    else:
        return y

print(max(4,7))
z = max(8,5)
print(z)





#Fill in the blanks to define a function that compares the lengths of its arguments and returns the shortest one.


def shortest_stringORlist(x,y):
    if len(x) <= len(y):
        return x
    else:
        return y

print(shortest_stringORlist([1,2,3],[1,2,3,4]))





"""#Once you return a value from a function, it immediately stops being executed.

Any code placed after the return statement won’t be executed.
For example:"""


def add_numbers(x,y):
    total = x + y
    return total
    print("this won't be printed")

print(add_numbers(4,5))



def print_numbers():
  print(1)
  print(2)
  return
  print(4)
  print(6)
print_numbers()



#Rearrange the code to define a function that calculates the sum of all numbers from 0 to its argument.




def sum(x):
    res =0
    for i in range(x):
        res +=i
    return res
print(sum(10))

