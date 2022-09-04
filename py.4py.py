#WHILE LOOPS


#A while loop is used to repeat a block of code multiple times.
#For example, let's say we need to process multiple user inputs, so that each time the user inputs something, the same block of code needs to execute.

#Below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates.


z= 1
while z <= 5:
    print(z)
    z=z+1                    #During each loop iteration, the i variable will get incremented by one, until it reaches 5.
                              #  So, the loop will execute the print statement 5 times.print("finished")
print("finished")




o= 5
while o <=100:          #The code in the body of a while loop is executed repeatedly. This is called iteration.
    print(o)
    o*=2      # increment




a = 3
while a>=0:
   print(a)
   a = a - 1   # increment




#You can use multiple statements in the while loop.
#For example, you can use an if statement to make decisions.
# This can be useful, if you are making a game and need to loop through a number of player actions and add or remove points of the player.
#The code below uses an if/else statement inside a while loop to separate the even and odd numbers in the range of 1 to 10:


x=1
while x<10:
    if x%2 == 0:
        print(str(x)+"is even")
    else:
        print(str(x)+ "is odd")

    x +=1   #increment





y = 20
while y <50:
    if y%2 == 0:
        print(str(y)+"is even")
    else:
        print(str(y)+ "is odd")

    y+= 5   #increment



# BREAK

#To end a while loop prematurely, the break statement can be used.
#For example, we can break an infinite loop if some condition is met:

b=0
while True:
    print(b)
    b=b +1   # increment
    if b>=5:
        print("breaking")
        break

print("finished")





#CONTINUE

#Another statement that can be used within loops is continue.
#Unlike break, continue jumps back to the top of the loop, rather than stopping it. Basically, the continue statement stops the current iteration and continues with the next one.




i = 0
while True:
    i = i +1             #while true  i creste in incremente de  +1 in while statement
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")






c= 1
while c<=5:           # verifica c pe fiecare linie
 #   print (c)# pritns 'c' bevore the if statement
    c+= 1
    if c==3:
        print("skipping 3")
        continue       # Ce face continue ?

    print(c)         #   prints c abter the continue
print("finished")



