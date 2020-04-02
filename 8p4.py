'''Exercise 8.4 COMPLETED'''
'''Lesson learned: In this file, there are two
different iterations. First you do the iterations
for the entire file and make the line a list, then you
go through that list and apped it to the lst list. but you
check each word and see if it is not in there. That is
all well and good. however, some of the methods you call
have different ways to implement them. for instance, .split
will only make a copy. you actually have to assign it to
a new variable. that is not true with sort. sort changes
the original lst and keeps it as such. Play around with
that'''

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    newlst = line.split()
    for word in newlst:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
