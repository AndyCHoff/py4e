#Exercise 6.6 Just messing around. Completed

cats = input("Enter a word please: ")

#Capitalizes the first letter of the first word only. not multiple words
print(cats.capitalize())
#Makes all letters small case
print(cats.casefold())
#Centers the word. The number you put in () is the length it is centered on
print(cats.center(25))
#Counts the number of times 'd' is in the word typed. Can count multiple words. Case sensitive.
print(cats.count("d"))
#Checks last letter (can be more than one letter). You can also slice the string and check that slice for the end values you want. Returns true/false. Case sensitive and returns a -1 if it does not find it.
print(cats.endswith("y"))
#Returns the location of the first instance of what you're trying to find. Case sensitive.
print(cats.find("y"))
#The curly brace is where you will replace the word.
newcats = "For only {cats} can enter the building"
print(newcats.format(cats=cats))
#checks to see if input is alpha numeric
print(cats.isalnum())
#check to see if input is all letters
print(cats.isalpha())
#checks to see if the word is all lower case
print(cats.islower())
#checks to see if input is numbers. Int not float.
print(cats.isnumeric())
#check is there is only white space in input
print(cats.isspace())
#Checks if you've got title Case
print(cats.istitle())
#checks if it is all upper case
print(cats.isupper())
#prints all words with title case
print(cats.title())
