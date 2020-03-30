#Exercise 3.1 Completed
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per Hour")
r = float(rate)

if h <=40:
    print(r*h)
else:
    newhours = h-40
    totalhours = (40*r)+(newhours*r*1.5)
    print(totalhours)
