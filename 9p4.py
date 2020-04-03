#Exercise 9.4
'''Add code to the below program to figure out
who has the most messages in the file. After all
the data has been read and the dic- tionary has been
created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to
find who has the most messages and print how many
messages the person has.'''

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
    fh = open(fname)
    daysofweek = dict()
    for line in fh:
        if not line.startswith("From ") :
            continue
        new = line.split()
        if new[1] not in daysofweek:
            daysofweek[new[1]] = 1
        else:
            daysofweek[new[1]] +=1
    largest = None
    for aaa,bbb in daysofweek.items():
        if largest is None or bbb>largest:
            email = aaa
            largest = bbb
print(email, largest)
