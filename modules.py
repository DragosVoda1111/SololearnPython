#MODULES

"""Modules are pieces of code that other people have written to fulfill common tasks, such as generating random numbers, performing mathematical operations, etc.

The basic way to use a module is to add import module_name at the top of your code, and then using module_name.var to access functions and values with the name var in the module.
For example, the following example uses the random module to generate random numbers:"""


import random

for i in range (2):
    value = random.randint(1,6)
    print(value)

#The code uses the randint function defined in the random module to print 2 random numbers in the range 1 to 6.  AKA dice baby!


import math
num = 10
(print(math.sqrt(num)))






"""There is another kind of import that can be used if you only need certain functions from a module.
These take the form from module_name import var, and then var can be used as if it were defined normally in your code.
For example, to import only the pi constant from the math module:"""


from math import pi

print(pi)



from math import sqrt
num=10
print(sqrt(num))


#Use a comma separated list to import multiple objects. For example:     from math import pi, sqrt

# '*' imports all objects from a module. For example: from math import *
#This is generally discouraged, as it confuses variables in your code with variables in the external module.



#TIP : You can import a module or object under a different name using the "as" keyword. This is mainly used when a module or object has a long or confusing name.

from math import sqrt as square_root
print(square_root(100))

"""There are three main types of modules in Python, those you write yourself, those you install from external sources, and those that are preinstalled with Python.
The last type is called the standard library, and contains many useful modules. Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

Tasks that can be done by the standard library include string parsing, data serialization, testing, debugging and manipulating dates, emails, command line arguments, and much more!
"""




"""Many third-party Python modules are stored on the Python Package Index (PyPI).
The best way to install these is using a program called pip. This comes installed by default with modern distributions of Python. If you don't have it, it is easy to install online. Once you have it, installing libraries from PyPI is easy. Look up the name of the library you want to install, go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name. Once you've done this, import the library and use it in your code.

Using pip is the standard way of installing libraries on most operating systems, but some libraries have prebuilt binaries for Windows. These are normal executable files that let you install libraries with a GUI the same way you would install other programs."""