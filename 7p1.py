#Exercise 7.1

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line=line.rstrip()
    newline=line.find(":")
    confi=float(line[newline+1:])
    total = total + confi
    count = count+1
print("Average spam confidence:", (total/count))
