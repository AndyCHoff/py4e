#playing around with methods
#this will sort the list and save it to x
x = [1, 2, 1, 4, 5, 6, 9, 234 ,4]
x.sort()
print(x)

#this will split the line of text into a list but you
#have to save it to a new variable
cats = 'murder was the case that they gave me'
newcats = cats.split()
print(newcats)


#so if you wanted to combine BOTH, you would create
#a new variable to put the list in, then sort.
sam = "aint nothin but a g thang babayyyyy"
newsam = sam.split()
newsam.sort()
print(newsam)
