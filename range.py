numbers = list(range(10))
print(numbers)

#In order to output the range as a list, we need to explicitly convert it to a list, using the list() function.

nums = list(range(5))
print(nums[4])



#If range is called with one argument, it produces an object with values from 0 to that argument.
#If it is called with two arguments, it produces values from the first to the second.


numbers =list(range(3,8))       #Remember, the second argument is not included in the range, so range(3, 8) will not include the number 8.
print(numbers)



print(range(20)  == range(0,20))



#random exercise
nums = list(range(5, 8))
print(len(nums))


#range can have a third argument, which determines the interval of the sequence produced, also called the step.

numbers1= list(range(5,20,2))
print(numbers1)


#We can also create list of decreasing numbers, using a negative number as the third argument, for example list(range(20, 5, -2))


numbers2= list(range(20,5,-2))
print(numbers2)


#random exercise
#What is the result of this code?
nums2 = list(range(3, 15, 3))
print(nums2[2])


#FOR LOOPS
#The for loop is commonly used to repeat some code a certain number of times. This is done by combining for loops with range objects.

for i in range(5):
    print(i)        #You don't need to call list on the range object when it is used in a for loop, because it isn't being indexed, so a list isn't required.




#random exercise
#Fill in the blanks to create a for loop that prints only the even values in the range:
for i in range(0, 20, 2):
    print(i)


#random execrcise
#What is the output of this code?

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

newIndex = list[4]       # ca sa intelegi mai bine separa primu list interior list[4] l-am ranumit newindex. valuarea lui e 5 in lista.
print(list[newIndex])       #dupa care faci listu exterior cu noua valoare 5 devine indexu car e pozitia 6 si pe pozitia 6 e numaru 8 in lista



#random exercise
for i in range(10):      #good luck with this shit :)))))
  if not i % 2 == 0:        #prints all even numbers between 2 and 10
    print(i+1)


#random exercise
#Fill in the blanks to print the first element of the list, if it contains even number of elements.
list = [1, 2, 3, 4]

if len(list) % 2 == 0:
 print(list[0])
