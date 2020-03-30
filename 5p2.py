#Exercise 5.2 Completed

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        newnum = int(num)
    except:
        print("Invalid Input")
        continue


    if largest is None:
        largest = newnum
    elif newnum > largest:
        largest = newnum
    if smallest is None:
        smallest = newnum
    elif newnum < smallest:
        smallest = newnum


print("Maximum", largest)
print("Minimum", smallest)
