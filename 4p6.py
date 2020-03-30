#Exercise 4.6
def computepay(h,r):
    if h > 40:
        total = (40*r)+((h-40)*r*1.5)
    else:
        total = h*r
    return total


hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))
p = computepay(hours,rate)
print ("Pay",p)
