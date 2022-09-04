# LISTS

"""At their simplest, Lists are used to store items.

We can create a list by using square brackets with commas separating items. Like this:"""


words = ["Hello","world","!"]




"""In that example the words list contains three string items: hello, world and !

If you want to access a certain item in the list, you can do this by using its index in square brackets. In our example, that would look like this:

For example:
"""


words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])





"""But lists aren’t just for shopping!

We can do some pretty cool stuff with them in Python. For example, we can use nested lists to represent 2D grids, such as matrices.

For example:
"""

                            #This is useful because a matrix-like structure can allow you to store data in row-column format,
                                   # like in ticketing programs, that need to store the seat numbers in a matrix, with their corresponding rows and numbers.
m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(m[1][2])




"""Strings can be indexed like lists too!

Indexing a string is like creating a list containing each character in the string.

For example:
"""



str = "hello world!"                     #space is also a symbol and has an index
print(str[6])




"""The list of cool things we can do with lists just keeps growing!
Lists can also be added and multiplied in the same way as strings."""

nums = [1, 2, 3]                              #Lists and strings share a lot of similarities - you can basically think of strings as lists of characters that can't be changed.
print(nums + [4, 5, 6])
print(nums * 3)





# LIST SLICES

"""further than List slices!

The most basic list slicing involves indexing a list with two colon-separated integers. This will return a new list containing all the values in the old list between the indices.

Example:
"""


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])                            #Just like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.
print(squares[3:8])
print(squares[0:1])

