# MULTIPLE OPERATORS AND CONDITIONS
# OPERATOR PRECEDENCE


print(False == False or True)

print(False == (False or True))

print((False == False)or True)


if 1 + 1 * 3 == 6:
   print("Yes")
else:
   print("No")




#chaining multiple conditions



grade = 88
if(grade >= 70 and grade <=100):
   print("Passed!")




x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")




# LISTS




words=["hello", " world","!"]    # pozitia fiecarui item in lista se numeste indexu itemului. Aici [ 0,1,2]
print(words[0])
print(words[1])
print(words[2])
print(words)



empty_list=[]
print(empty_list)




number=3
things= ["string",0 , [1,2,number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])    # index 2 din lista 2

m = [              # Nested lists can be used to represent 2D grids, such as matrices.
   [1,2,3],         #A matrix-like structure can be used in cases where you need to store data in row-column format.
   [4,5,6]          #For example, when creating a ticketing program, the seat numbers can be stored in a matrix, with their corresponding rows and numbers.
   ]

print(m[1][2])   # index 2 din lista 1
                  #The code above outputs the 3rd item of the 2nd row.



variable= "hello world!"
print(variable[6])   #  'w'  e pe index 6 din lista variable. ( space is also a symbol and has an index)



num = [5, 4, 3, [2], 1]
print(num[2])
print(num[3])



# LIST OERATIONS



nums=[7,7,7,7,7]   # The item at a certain index in a list can be reassigned.
nums[2] = 5
print(nums)


nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])




#Lists can be added and multiplied in the same way as strings


nums2=[1,2,3]
print(nums2 + [4,5,6])
print(nums*3)


#To check if an item is in a list, the in operator can be used.
#It returns True if the item occurs one or more times in the list, and False if it doesn't.


words2= ["spam", "eggs","sausage"]
print("spam" in words2)
print("eggs" in words2)
print("tomato" in words2)





nums3 = [10, 9, 8, 7, 6, 5]
nums3[0] = nums3[1] - 5
if 4 in nums3:
  print(nums3[3])
else:
  print(nums3[4])


#To check if an item is not in a list, you can use the not operator in one of the following ways:


nums4= [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)



# LIST FUNCTIONS

#The append method adds an item to the end of an existing list.


nums5= [1,2,3]
nums5.append(4)             # The dot before append is there because it is a method of the list class. Methods will be explained in a later lesson.
print(nums5)



words6=["hello"]
words6.append('world')
print(words6[1])


nums7 = [1,3,5,2,4]             #To get the number of items in a list, you can use the len function.
print(len(nums))



letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))


#The insert method is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.


words7=["python","fun"]
index=1
words7.insert(index, "is")
print(words7)


words7.insert(0,"is")
print(words7)


nums8 = [9, 8, 7, 6, 5]
nums8.append(4)
nums8.insert(2, 11)
print(len(nums8))

print(nums8[3])       #insert muta indexu fiecarei valori dupa insert cu una la dreapta ... logic...




#The index method finds the first occurrence of a list item and returns its index.


letters2=['p','q','r','s','p','u']
print(letters2.index('r'))
print(letters2.index('p'))
print(letters2.index('u'))


#There are a few more useful functions and methods for lists.

#max(list): Returns the list item with the maximum value
#min(list): Returns the list item with minimum value
#list.count(item): Returns a count of how many times an item occurs in a list

print(letters2.count("p"))
print(letters2.count('r'))

#list.remove(item): Removes an object from a list


#list.reverse(): Reverses items in a list.

