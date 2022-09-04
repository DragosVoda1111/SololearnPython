#You've already used functions in previous lessons.
#Any statement that consists of a word followed by information in parentheses is a function call.
#Here are some examples that you've already seen:

print("Hello world!")           #The words in front of the parentheses are function names, and the comma-separated values inside the parentheses are function arguments.
range(2, 20)
str(12)
range(10, 20, 3)

#In addition to using pre-defined functions, you can create your own functions by using the def statement.
#Here is an example of a function named my_func. It takes no arguments, and prints "spam" three times. It is defined, and then called.
#The statements in the function are executed only when the function is called.

def my_func():                  #The code block within every function starts with a colon (:) and is indented.
    print("spam")
    print("spam")
    print("spam")

my_func()





def sayHi():
    print("Hi!")

sayHi()


#All the function definitions we've looked at so far have been functions of zero arguments, which are called with empty parentheses.
#However, most functions take arguments.
#The example below defines a function that takes one argument:


def print_with_exclamation(something):              #something is a ARGUMENTS
    print(something + "!")


print_with_exclamation("spam")                       # spam, eggs python are PARAMETERS
print_with_exclamation("eggs")
print_with_exclamation("python")




def print_double(x):
    print(2*x)

print_double(3)



#You can also define functions with more than one argument; separate them with commas.

def print_sum_twice(x,y):
    print(x+y)
    print(x+y)

print_sum_twice(5,8)           #argument values are defined when "calling" the function



#Function arguments can be used as variables inside the function definition.
# However, they cannot be referenced outside of the function's definition. This also applies to other variables created inside a function.

def function(variable):              #variable is a ARGUMENT
    variable +=1                     #works only before the "calling" on the function
    print(variable)

function(7)                           # 7 is an PARAMETER

#Technically, parameters are the variables in a function definition, and arguments are the values put into parameters when functions are called.





#Fill in the blanks to define a function that prints "Yes", if its parameter is an even number, and "No" otherwise.
def even(x):
    if x%2 == 0:
        print("yes")
    else:
        print("no")

even(2)



#RETURNING FROM FUNCTIONS
#Certain functions, such as int or str, return a value that can be used later.
#To do this for your defined functions, you can use the return statement.


def max(x,y):
    if x>=y:
        return x
    else:
        return y

print(max(4,7))
z= max(8,5)
print(z)


#RANDOM EXERCISE
# Fill in the blanks to define a function that compares the leghts of its arguments and returns the shortest one.

def shortest_string(x,y):
  if len(x) <= len(y):
    return x
  else:
    return y

print(shortest_string("abc","ab"))



#exercise
def chestie(name):
    print("hey there"+name)

chestie(" Dragos")


#Although they are created differently from normal variables, functions are just like any other kind of value.
#They can be assigned and reassigned to variables, and later referenced by those names.


def multiply(x,y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a,b))






def shout(word):
    return word+ "!"
speak = shout
output= speak("shout")
print(output)





def cube(num):
    return num*num*num

result = cube(4)
print(result)



#Functions can also be used as arguments of other functions.

def add(x, y):
    return x + y

def do_twice(func, x, y):                           # the "add" parameter in print represents the value for the "func" argument in do_twice
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
