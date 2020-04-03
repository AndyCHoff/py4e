#Exercise 9.2 Completed!

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
    fh = open(fname)
    daysofweek = dict()
    for line in fh:
        if not line.startswith("From ") :
            continue
        new = line.split()
        newlist = new[2]
        daysofweek[newlist] = daysofweek.get(newlist,0)+1
print(daysofweek)
