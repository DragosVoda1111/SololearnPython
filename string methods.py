#FIND METHOD
# string.find(substring, start, end)


my_string = "Where's Waldo?"



x = my_string.find("Waldo")
print(x)


y = my_string.find("Wenda")
print(y)


z = my_string.find("Waldo", 0, 13)
print(z)




# INDEX METHOD
# string.index(substring, start, end)


a = my_string.index("Waldo")
print(a)
print(" just above is 'a' value")


try:

    my_string.index("Wenda")
except ValueError:
    print("not found")




# COUNT METHOD
#string.count(substring, start, end)



my_string = "How many fruits do you have in your fruit basket"
b = my_string.count("fruit")
print(b)


c = my_string.count("fruit", 0, 14)
print(c)


#REPLACE METHOD
#string.replace(old, new, count)


my_string = "The red house is between the blue house and the old house"
print(my_string.replace("house", "car", 2))