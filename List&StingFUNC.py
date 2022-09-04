# functions

#functions supported by lists
#append
nums = [1,2,3]
nums.append(4)
print(nums)

#insert
words = ["python","fun"]
index = 1
words.insert(index,"is")
print(words)

words.insert(1,"is")
print(words)




# index

letters = ['p','q','r','s','t','u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('r'))





lis = [1,2,3,4,5,6,7,8,9]

print(max(lis))

"""max(list): Returns the maximum value.
min(list): Returns the minimum value.
list.count(item): Returns a count of how many times an item occurs in a list.
list.remove(item): Removes an item from a list.
list.reverse(): Reverses items in a list."""

#For example, you can count how many 42s are there in the list using:
#items.count(42) where items is the name of our list.





# STRING FORMATING
"""

Strings have a format() function, which enables values to be embedded in it, using placeholders.

Example:"""

nums = [4,5,6]
msg = "Numbers: {0} {1} {2}". format(nums[0],nums[1],nums[2])        #Each argument of the format function is placed in the string at the corresponding position,
                                                                      # which is determined using the curly braces { }.
print(msg)



#You can also name the placeholders, instead of the index numbers.


str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)



"""
Another lightning round! Here are some of the other useful string functions:

join - joins a list of strings with another string as a separator.

replace - replaces one substring in a string with another.

startswith and endswith - determine if there is a substring at the start and end of a string, respectively.

lower and upper – changes the case of a string

split -the opposite of join, turns a string with a certain separator into a list.
Here they are in action:"""


print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

