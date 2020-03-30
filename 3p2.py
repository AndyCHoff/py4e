#Exercise 3.2 = This exercise can be modified in the future. The program should quit when the first invalid input is given. The way it currently stands, is that both inputs are given, and it ignores whether or not the input is valid. Then after both inputs are given THEN the error message is given to the correct one that was wrong.

hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

try:
    h = float(hrs)
except:
    print("This input is not valid for Hours")
    pass

try:
    r = float(rate)
except:
    print("This input is not valid for Rate")
    exit()

if h <=40:
    print(r*h)
else:
    newhours = h-40
    totalhours = (40*r)+(newhours*r*1.5)
    print(totalhours)
