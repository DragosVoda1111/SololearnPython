def sum_up(val1, val2):
    return val1 + val2

def do_something(foo, val1, val2):
    return foo(val1,val2)

print(do_something(sum_up,5,2))            # 5 and 2 are 7 but sum up is allready 7? why is the output 7 and not 14?
                                    #pt ca "sum_up" function as parameter, only defines wich function is used as a parameter in the last function. because you can CHOOSE multiple.
                                    #(other than "sum_up" you can have a different one ).
                                    # and then the values 2,5 are the the parameters that are assigned as arguments to that CHOSEN function




def square(x):
    return x*x

def test(func,x):
    print(func(x))                #why  func(x) ? why parantheses

test(square,42)







def add(x,y):
  return x +y


def do_twice(func,x,y):
  return func(func(x, y),func(x,y))

a= 5
b= 10

print(do_twice(add,a,b))




#__________________________________________________________________________________________________________











#Rearrange the code to define a function that calculates the sum of all numbers from 0 to its argument.


def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(sum(7))





#same shit, why 0?

def print_nums(x):
    for i in range(x):
        print(i)
    return

print_nums(10)









# WTF up with this one boiiiii




i = 1
while i<6:
    print(i)
    i +=1
    if i == 3:       #this one is 1 , 2
        break


i = 1
while 1<6:
    print(i)
    if i ==3:
        break        # this one is 1, 2,3           why?
    i+=1
