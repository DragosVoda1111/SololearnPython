# FOR LOOPS

#The for loop is used to iterate over a given sequence, such as lists or strings.
#The code below outputs each item in the list and adds an exclamation mark at the end:



words = ["hello","world","spam","eggs"]
for word in words:   # word seems to become a variable representing each index of the sequence
    print(word+'!')

#In the code above, the word variable represents the corresponding item of the list in each iteration of the loop.
#During the 1st iteration, word is equal to "hello", and during the 2nd iteration it's equal to "world", and so on.





#The for loop can be used to iterate over strings.

str1 = "testing for loops"
count = 0

for x in str1:
    if(x == 't'):
        count +=1

print(count)

#The code above defines a count variable, iterates over the string and calculates the count of 't' letters in it. During each iteration, the x variable represents the current letter of the string.
#The count variable is incremented each time the letter 't' is found, thus, at the end of the loop it represents the number of 't' letters in the string.



list=[2,3,4,5,6,7]

for x in list:
    if(x%2== 1 and x>4):
        print(x)
        break                          # cu break la primu raspuns corect , 5





list=[2,3,4,5,6,7]

for x in list:
    if(x%2== 1 and x>4):
        print(x)
        continue                         # cu continue  ca sa ia si 5 si 7



#for vs while


#Both, for and while loops can be used to execute a block of code for multiple times.

#It is common to use the for loop when the number of iterations is fixed. For example, iterating over a fixed list of items in a shopping list.

#The while loop is used in cases when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop.
#For example, ending the loop when the user enters a specific input in a calculator program.

#Both, for and while loops can be used to achieve the same results, however, the for loop has cleaner and shorter syntax, making it a better choice in most cases.