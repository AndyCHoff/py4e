#Exercise 9.3 COMPLETED YOOOOOOOOOO
'''Write a program to read through a mail log,
build a histogram using a dictionary to count
how many messages have come from each email address,
and print the dictionary.'''


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
print(daysofweek)
