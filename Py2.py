#in place operators
#X = X + un value :  x + = un value

x= 2
print(x)



x+= 3
print(x)



x*= 2
print(x)



x1=4
x1*=3
print(x1)




x2= "spam"
print(x2)



x2 += "eggs"
print(x2)




x3 = 20
print(x3)




x3 /= 6
print(x3)




x4 = 20

x4 %= 6
print(x4)



x5= "a"
x5 *= 3
print(x5)



spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))




penis= "10"
penis= penis + "5"
mata= int(penis) + 3
print("mata e " +str(mata)) # nu ma lasa sa printez stringuri + float sau int (float sau int trebuie sa fie fara un mesaj string inauntru unui print)



x = 5
y = x + 3
y = int(str(y) + "2")
print(y)



# BOOLEANS : True or False



myboolean = True
print(myboolean)

print(2==3)

print("hello"=="hello")

#not equal booleans  !=

print( 1 != 1)

print("eleven" !=  "seven")

print(2 != 10)

# comparison booleans  >  <

print( 7 > 5 )

print (10<10)

print ( 50 > 49.99)

# greater/smaller than booleans   >=  <=

print(7 <= 8)

print(9  >= 9.0)

# lexicographical comparison booleans


print("c">"b")  #true

print("a" > "x") #false

print("annie" > "andy") #true : n > d



# IF STATEMENTS



if 10 > 5: # asta e un expression
    print("10 greater than 5") #asta e un statement

print("program ended")

spam2=7
if spam2 > 5:
   print("eight")


num = 12
if num> 5:
    print("bigger than 5")
    if num <=47:
        print("betwwen 5 and 47")


num2 = 7
if num2 > 3:
   print("3")
   if num2 < 5:
      print("5")
      if num2 ==7:
         print("7")  # de ce imi da 3 aici  si 7 jos


num3 = 7
if num3 ==7:
    print('7')        # ???????????????



#ELSE STATEMENTS


x1 = 4
if x1 == 5:
    print("yes")
else:
    print("no")


if 1 + 1 == 2:
   if 2 * 2 == 8:
      print('if')
   else:
      print("else")


num5= 3
if num5  == 1:
    print("one")
else:
    if num5 == 2:
        print("two")
    else:
        if num5 ==3:
            print("three")
        else:
            print("Something else")


num6 = 3
if num6 == 1:
    print("one")
elif num6 == 2:
    print("two")
elif num6 == 3:
    print("three")
else:
    print("something else")


#BOOLEAN LOGIC


print(1 == 1 and 2==2)

print( 1 == 1 and  2==3)


print(1 != 1 and 2==2)

print(2<1 and 3>6)





print(1==1 or 2==2)

print(1 ==1 or 2== 3)

print(1 != 1 or 2 == 2)

print(2< 1 or 3> 6)





print(not 1 == 1)

print(not 1>7)

print("stop aici")





if not True:         #"True" e un true Boolean in itself ca si   1 == 1
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")


if True:
    print("1")


