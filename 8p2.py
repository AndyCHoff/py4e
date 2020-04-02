#exercise 8.2 completed we figured that if the only
#word that was in there was 'From' then it would fail
#because there would be a range error
'''Figure out which line of the above program
is still not properly guarded. See if you can
construct a text file which causes the program to
fail and then modify the program so that the line is
properly guarded and test it to make sure it handles
your new text file.'''


fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 :
        continue
    if len(words) < 3:
        continue
    if words[0] != 'From' :
        continue
    print(words[2])
