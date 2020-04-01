#Exercise 8.4 COMPLETED BUT>>>>
#try to do this one on your own
# you got this from github no cheating.
#try to implement the way of thinking here


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
