#Exercise 5.1 Completed

total = None
count = None
avg = None

while True:
    num = input("Enter a number ")
    if num == "done":
        break
    try:
        newnum = int(num)
    except:
        print("Invalid Data")
        continue

    if total == None:
        total = newnum
    else:
        total = total + newnum
    if count == None:
        count = 1
    else:
        count = count + 1
    if avg == None:
        avg = newnum
    else:
        avg = total/count

print(total, count, avg)
