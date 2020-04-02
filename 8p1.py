#exercise 8.1 completed!!! 

'''Exercise 1: Write a function called
chop that takes a list and modifies it,
removing the first and last elements, and
returns None. Then write a function called
middle that takes a list and returns a new
list that contains all but the first and
last elements.'''

def chop(num):
    del num[0]
    del num[-1]
    print(num)

def middl(middler):
    del middler[1:-1]
    print(middler)

new = ["new","newnew", "old", "cant", "wont", "dont"]
newnew = ["new","newnew", "old", "cant", "wont", "dont"]
chop(new)
middl(newnew)
