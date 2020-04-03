#exercise 9.1 Completed!!!
#i have no idea what the flippin flap
#I'm doing here. UGHGHGHHGHGHGHGH. Turns out you did.
#you just forgot one simple syntax thing. You won't
#forget it now will ya WILL YA!?!?!?!?
'''
Write a program that reads the words in words.txt
and stores them as keys in a dictionary. It doesn’t
matter what the values are. Then you can use the
in operator as a fast way to check whether a string
is in the dictionary.
'''
fhand = input("Enter a text file name: ")
fname = open(fhand)
newdic = dict()
for line in fname:
    lines = line.split()
    for word in lines:
        if word not in newdic:
            newdic[word] = 1
        else:
            newdic[word] +=1
print(newdic)
