# 1
text = input()
word = input()
def search(x,y):
    if "this is awesome" in x and "awesome" in y:
        print("word found")
    else:
        print("word not found")

print(search(text,word))



#2
text = input()
word = input()
def search(x,y):
  if x == "This is awsome" and y == "awsome":
         print("Word Found")
  else:
         print("Word not found")


print(search(text, word))


#3
text = input()
word = input()
def search(x,y):
    if x.find("") >=1 and y.find("") >=1:
        print("Word found")
    else:
        print("word not found")
print(search(text,word))