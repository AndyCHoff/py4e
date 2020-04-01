#Exercise 7.1 completed


fname = open("mbox-short.txt")
for line in fname:
    new=line.rstrip().upper()
    print(new)
